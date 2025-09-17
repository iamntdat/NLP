from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.core.dataset_loaders import load_raw_text_data

def test_tokenizers():
    # Instantiate tokenizers
    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()
    
    # Test sentences
    sentences = [
        "Hello, world! This is a test.",
        "NLP is fascinating... isn't it?",
        "Let's see how it handles 123 numbers and punctuation!"
    ]
    
    # Test on provided sentences
    print("Testing on Provided Sentences:")
    print("\nSimpleTokenizer Results:")
    for sentence in sentences:
        tokens = simple_tokenizer.tokenize(sentence)
        print(f"Input: {sentence}\nOutput: {tokens}\n")
    
    print("RegexTokenizer Results:")
    for sentence in sentences:
        tokens = regex_tokenizer.tokenize(sentence)
        print(f"Input: {sentence}\nOutput: {tokens}\n")
    
    # Test on UD_English-EWT dataset
    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    dataset_path = r"D:\Download\UD_English-EWT\UD_English-EWT\en_ewt-ud-train.txt"
    try:
        raw_text = load_raw_text_data(dataset_path)
        sample_text = raw_text[:500]  # First 500 characters
        print(f"Original Sample: {sample_text[:100]}...")
        
        simple_tokens = simple_tokenizer.tokenize(sample_text)
        print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")
        
        regex_tokens = regex_tokenizer.tokenize(sample_text)
        print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")
    except FileNotFoundError:
        print(f"Error: Dataset path '{dataset_path}' not found.")
    except Exception as e:
        print(f"Error loading dataset: {e}")

if __name__ == "__main__":
    test_tokenizers()