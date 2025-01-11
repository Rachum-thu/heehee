import os
import time
import json
import logging
import asyncio
from typing import Literal, List, Dict
from chat_parallel import process_api_requests_from_file

# Constants
CACHE_DIR = '.cache'
RATE_LIMIT = {
    "tier4": {
        'gpt-4o-mini': {'PRM': 10_000, "TPM": 10_000_000}
    }
}
VALID_MODELS = {'gpt-4o', 'gpt-4o-mini'}
VALID_TIERS = {'tier1', 'tier2', 'tier3', 'tier4', 'tier5'}

# Utility Functions
def validate_inputs(model_name: str, tier_list: str):
    """Validate model_name and tier_list against allowed values."""
    if model_name not in VALID_MODELS:
        raise ValueError(f"Invalid model_name: {model_name}. Must be one of {VALID_MODELS}.")
    if tier_list not in VALID_TIERS:
        raise ValueError(f"Invalid tier_list: {tier_list}. Must be one of {VALID_TIERS}.")

def create_request_file(inputs: List[str], model_name: str, params: Dict) -> str:
    """Generate the request JSONL file."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    request_file = f'{CACHE_DIR}/request_{timestamp}.jsonl'

    content = [
        {
            'model': model_name,
            'messages': [{'role': "user", 'content': input_text}],
            **params
        }
        for input_text in inputs
    ]

    with open(request_file, 'w') as f:
        for instance in content:
            f.write(json.dumps(instance) + '\n')

    return request_file

def read_responses(save_file: str) -> List[str]:
    """Read and parse responses from the response JSONL file."""
    responses = []
    with open(save_file, 'r') as f:
        for line in f:
            responses.append(json.loads(line))

    return [
        response['choices'][0]['message']['content']
        for response in responses
    ]

# Main Chat Function
def chat(
    inputs: List[str],
    model_name: Literal['gpt-4o', 'gpt-4o-mini'] = 'gpt-4o-mini',
    tier_list: Literal['tier1', 'tier2', 'tier3', 'tier4', 'tier5'] = 'tier4',
    **params
) -> List[str]:
    """Main chat function with runtime validation and processing."""
    validate_inputs(model_name, tier_list)

    # File paths
    request_file = create_request_file(inputs, model_name, params)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    save_file = f'{CACHE_DIR}/response_{timestamp}.jsonl'

    # Process API requests
    asyncio.run(
        process_api_requests_from_file(
            requests_filepath=request_file,
            save_filepath=save_file,
            request_url="https://api.openai.com/v1/chat/completions",
            api_key=os.environ['OPENAI_API_KEY'],
            max_requests_per_minute=RATE_LIMIT[tier_list][model_name]['PRM'],
            max_tokens_per_minute=RATE_LIMIT[tier_list][model_name]['TPM'],
            token_encoding_name='o200k_base',
            max_attempts=5,
            logging_level=logging.INFO
        )
    )

    # Extract and return responses
    return read_responses(save_file)

# Entry Point
if __name__ == '__main__':
    try:
        responses = chat(['Who is your daddy?', 'What is the meaning of life?'])
        for response in responses:
            print(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
