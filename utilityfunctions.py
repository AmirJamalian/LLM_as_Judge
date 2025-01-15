import re
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_float(item):
    float_pattern = r'-?\d+\.\d+'
    item = str(item)
    float_values = re.findall(float_pattern, item)
    float_values = [float(value) for value in float_values]
    if len(float_values) == 0:
        return None
    else:
        return float_values[0]

def generate_topic(example_topics=["AI", "ML"], model_type="gpt-3.5-turbo-0125", word_count=15):
    try:
        # Define the prompt
        prompt = (
            f"Consider these example topics, prepared for generating some essays: '{example_topics}'. "
            f"Suggest a topic (less than '{word_count}' words) like the given example but totally different from them in terms of context and area. "
        )

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model=model_type,
            messages=[
                {"role": "system", "content": "You are an expert in suggesting topics in various fields."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=word_count * 4 // 3,
            temperature=0.7                  # Adjust creativity level
        )

        # Extract and return the essay text
        topic = response['choices'][0]['message']['content'].strip()
        return topic

    except Exception as e:  # Catch generic exceptions
        return f"Error generating topic: {str(e)}"

def generate_essay(topic="AI and its Applications", model_type="gpt-3.5-turbo-0125", word_count=100):
    try:
        # Define the prompt
        prompt = (
            f"Write an essay about '{topic}'. "
            f"The essay should be approximately {word_count} words long."
        )

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model=model_type,
            messages=[
                {"role": "system", "content": "You are an essay writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=word_count * 4 // 3,  # Estimate tokens for word count
            temperature=0.7                  # Adjust creativity level
        )

        # Extract and return the essay text
        essay = response['choices'][0]['message']['content'].strip()
        return essay

    except Exception as e:  # Catch generic exceptions
        return f"Error generating essay: {str(e)}"

def evaluate_essay(essay, topic, model_type="gpt-4o"):
    try:
        # Define the prompt
        prompt = (
            f"You are an expert essay evaluator. Your task is to evaluate the quality of essays based on their relevance to the topic, coherence, organization, grammar, and depth of content."
            f" The scoring range is from 0.0 to 9.0, with 0.0 being the lowest quality and 9.0 being outstanding quality."
            f" Here is the topic: \"{topic}\"."
            f" Here is the essay:\n\n{essay}\n\n"
            f"Please provide a single numeric score (0.0 to 9.0) as the output."
        )

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model=model_type,
            messages=[
                {"role": "system", "content": "You evaluate essays based on quality and relevance to the topic."},
                {"role": "user", "content": prompt}
            ],
            # max_tokens = word_count
        )

        # Extract and return the essay text
        score = response['choices'][0]['message']['content'].strip()
        return score

    except Exception as e:  # Catch generic exceptions
        return f"Error generating score: {str(e)}"

