# CSV Format Test Examples

This folder demonstrates different ways to use CSV files for promptfoo test cases, based on the [official documentation](https://www.promptfoo.dev/docs/configuration/test-cases/#csv-format).

## Directory Structure

```
csv-format-example/
├── promptfooconfig.yaml              # Basic examples
├── promptfooconfig_fscore.yaml       # F-score classification example
├── FSCORE_COMPLETE_GUIDE.md          # Comprehensive F-score guide
├── README.md                         # This file
├── prompts/
│   ├── prompt.txt                    # General Q&A prompt
│   └── sentiment_prompt.txt          # Sentiment analysis prompt
└── tests/
    ├── basic_tests.csv                    # Simple question/answer format
    ├── tests_with_assertions.csv          # Single __expected assertion
    ├── tests_multiple_assertions.csv      # Multiple __expected1, __expected2, etc.
    ├── tests_with_metadata.csv            # With filterable metadata
    ├── tests_with_tags.csv                # With array metadata (tags)
    └── fscore_simple.csv                  # F-score sentiment classification
```

## CSV File Examples

### 1. Basic CSV (`basic_tests.csv`)
Simple format with variables automatically mapped from column headers:
```csv
question,expectedAnswer
"What is 2+2?","4"
"What is the capital of France?","Paris"
```

### 2. CSV with Assertions (`tests_with_assertions.csv`)
Uses `__expected` column for inline assertions:
```csv
input,__expected
"Hello world","contains: Hello"
"Calculate 5 * 6","equals: 30"
"What's the weather?","llm-rubric: Provides weather information"
```

### 3. Multiple Assertions (`tests_multiple_assertions.csv`)
Uses `__expected1`, `__expected2`, etc. for multiple assertions per test:
```csv
question,__expected1,__expected2,__expected3
"What is 2+2?","equals: 4","contains: four","javascript: output.length < 10"
```

### 4. CSV with Metadata (`tests_with_metadata.csv`)
Includes `__metadata:` columns for filtering tests:
```csv
question,__expected,__metadata:category,__metadata:difficulty
"What is 2+2?","equals: 4","math","easy"
"Explain quantum physics","llm-rubric: Accurate explanation","science","hard"
```

Filter tests by metadata:
```bash
promptfoo eval --filter-metadata category=math
promptfoo eval --filter-metadata difficulty=easy
```

### 5. CSV with Tags (`tests_with_tags.csv`)
Uses `__metadata:tags[]` for array metadata:
```csv
topic,__expected,__metadata:tags[]
"Machine learning","llm-rubric: Explains ML concepts","ai,technology,data science"
```

### 6. F-Score Classification (`fscore_simple.csv`)
Clean CSV format with just test data - assertions defined in config:
```csv
text,sentiment,__description
"This product is amazing!","positive","Positive: enthusiastic review"
"Terrible experience.","negative","Negative: strong disappointment"
"Best purchase ever!","positive","Positive: strong recommendation"
```

**How it works:**
- CSV contains only test data (text, expected sentiment, description)
- Assertions are defined once in `promptfooconfig_fscore.yaml` using `defaultTest`
- Tracks 4 metrics: Accuracy, True Positives (TP), False Positives (FP), False Negatives (FN)

**Calculated metrics:**
- **Precision** = TP / (TP + FP) - "Of all I said were positive, how many actually were?"
- **Recall** = TP / (TP + FN) - "Of all that were positive, how many did I catch?"
- **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall) - Harmonic mean balancing both

**📖 For complete F-score guide:** See [`FSCORE_COMPLETE_GUIDE.md`](./FSCORE_COMPLETE_GUIDE.md) for detailed explanations, real-world examples, implementation guide, and troubleshooting.

## Special CSV Columns

| Column | Purpose | Example |
|--------|---------|---------|
| `__expected` | Single assertion | `contains: Paris` |
| `__expected1`, `__expected2`, ... | Multiple assertions | `equals: 42` |
| `__description` | Test description | `Basic math test` |
| `__metadata:*` | Filterable metadata | `__metadata:category` |
| `__metadata:*[]` | Array metadata | `__metadata:tags[]` |
| `__prefix` | Prepend to prompt | `You must answer:` |
| `__suffix` | Append to prompt | `(be concise)` |
| `__threshold` | Pass threshold | `0.8` |

## Assertion Types in CSV

- `contains: text` - Output contains the text
- `icontains: text` - Case-insensitive contains
- `equals: text` - Exact match
- `contains-all: item1,item2` - Contains all items (comma-separated)
- `contains-any: item1,item2` - Contains any item (comma-separated)
- `llm-rubric: criteria` - LLM judges based on criteria
- `javascript: code` - JavaScript expression that returns true/false

## Setup

1. Install promptfoo:
```bash
npm install -g promptfoo
```

2. Set up environment:
```bash
cp env.example .env
# Edit .env with your API key
```

## Running Tests

### Basic Examples
Run with the default CSV file (basic_tests.csv):
```bash
cd csv-format-example
promptfoo eval
```

To test different CSV formats, edit `promptfooconfig.yaml` and uncomment the desired test file.

### F-Score Classification Example
Run the sentiment analysis with F-score metrics:
```bash
cd csv-format-example
promptfoo eval -c promptfooconfig_fscore.yaml
```

This will:
1. Analyze sentiment for each text sample
2. Track true positives, false positives, and false negatives
3. Calculate precision, recall, and F1 score automatically
4. Display the derived metrics in the results

View results:
```bash
promptfoo view
```

## Tips

1. **CSV is ideal for bulk test data** - Easy to create and maintain in spreadsheets
2. **Use metadata for organization** - Filter tests by category, difficulty, priority, etc.
3. **Combine assertion types** - Use multiple `__expected` columns for comprehensive testing
4. **Escape commas in values** - Use quotes: `"global\,warming"` for literal commas in metadata arrays
5. **Load multiple CSVs** - Use `file://tests/*.csv` to load all CSV files at once

## F-Score Use Cases

F-score is particularly useful for:

1. **Classification Tasks**: Sentiment analysis, intent detection, category assignment
2. **Imbalanced Datasets**: When some categories are rare and accuracy alone isn't enough
3. **Quality + Coverage**: When you need the model to be both accurate AND comprehensive
4. **Binary Classification**: Especially when false positives and false negatives have different costs

## Documentation

- **[FSCORE_COMPLETE_GUIDE.md](./FSCORE_COMPLETE_GUIDE.md)** - Comprehensive guide to F-score implementation
  - Simple explanations with real-world examples
  - Step-by-step implementation guide
  - Troubleshooting common issues
  - Advanced topics and tips

## References

- [Promptfoo CSV Format Documentation](https://www.promptfoo.dev/docs/configuration/test-cases/#csv-format)
- [Assertion Types](https://www.promptfoo.dev/docs/configuration/expected-outputs/)
- [F-Score Documentation](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/#f-score)
