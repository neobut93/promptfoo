# F-Score Complete Guide

A comprehensive guide to understanding and implementing F-score for classification tasks in promptfoo.

---

## Table of Contents

1. [Quick Start](#quick-start) (30 seconds)
2. [Simple Explanation](#simple-explanation) (5 minutes)
3. [Real-World Examples](#real-world-examples) (5 minutes)
4. [Implementation Guide](#implementation-guide) (10 minutes)
5. [Troubleshooting](#troubleshooting) (5 minutes)
6. [Advanced Topics](#advanced-topics)

---

## Quick Start

**What is F-Score?** A metric that measures how well your AI classifies things by balancing precision (accuracy) and recall (completeness).

**When to use it?** Sentiment analysis, spam detection, content moderation - any classification task where both false positives and false negatives matter.

**How it works:** Track 4 metrics → Calculate precision & recall → Get F1 score (0-1, higher is better)

**Jump to:** [Implementation Guide](#implementation-guide) for code examples.

---

## Simple Explanation

### What Are We Testing? (Like Teaching a Robot)

Imagine you're teaching a robot to sort toys into boxes: "happy toys" and "sad toys".

The robot looks at each toy and decides:
- 🟢 **"This is a HAPPY toy!"** (puts it in the happy box)
- 🔴 **"This is a SAD toy!"** (puts it in the sad box)

### The JavaScript Assertions (The Scorekeepers)

Think of these as little helpers that watch the robot and keep score. Each one counts different things:

#### 1. **Accuracy Counter** (Did the robot get it right?)
```javascript
output.sentiment === context.vars.sentiment
```
**In plain English:** "Is what the robot said the same as what it should be?"

**Example:** 
- Robot says: "Happy toy!" 
- Answer key says: "Happy toy!"
- ✅ Correct! Score = 1

---

#### 2. **True Positives Counter** (Correctly found the happy toys)
```javascript
output.sentiment === 'positive' && context.vars.sentiment === 'positive' ? 1 : 0
```
**In plain English:** "Did the robot say 'Happy' AND was it actually happy?"

**Example:**
- Robot says: "Happy toy!"
- Answer key: "Happy toy!"
- ✅ Good catch! Score = 1

**Another example:**
- Robot says: "Sad toy!"
- Answer key: "Happy toy!"
- ❌ Missed it! Score = 0

---

#### 3. **False Positives Counter** (Wrongly thought it was happy)
```javascript
output.sentiment === 'positive' && context.vars.sentiment === 'negative' ? 1 : 0
```
**In plain English:** "Did the robot say 'Happy' BUT it was actually sad?"

**Example:**
- Robot says: "Happy toy!"
- Answer key: "Sad toy!"
- ❌ False alarm! Score = 1 (we count mistakes)

---

#### 4. **False Negatives Counter** (Missed the happy toys)
```javascript
output.sentiment === 'negative' && context.vars.sentiment === 'positive' ? 1 : 0
```
**In plain English:** "Did the robot say 'Sad' BUT it was actually happy?"

**Example:**
- Robot says: "Sad toy!"
- Answer key: "Happy toy!"
- ❌ Missed it! Score = 1 (we count misses)

---

### What These Numbers Tell Us

After sorting 10 toys, we count up all the scores:

#### Precision (How careful is the robot?)
**Question:** "When the robot puts a toy in the happy box, how often is it REALLY happy?"

**Like:** A picky eater who only eats food they're 100% sure is yummy.
- **High Precision** = Very careful, rarely wrong, but might miss some happy toys
- **Low Precision** = Makes lots of mistakes, puts sad toys in happy box

---

#### Recall (How good is the robot at finding things?)
**Question:** "Of all the happy toys, how many did the robot actually find?"

**Like:** Finding all your socks in the laundry.
- **High Recall** = Finds most of the happy toys
- **Low Recall** = Misses many happy toys

---

#### F1 Score (Overall grade)
**Question:** "Is the robot both careful AND good at finding things?"

**Like:** A report card that combines two grades into one.
- **Score close to 1** = Excellent! 🌟
- **Score close to 0** = Needs practice 📚

---

## Real-World Examples

### 1. **Email Spam Filter** 📧
**The Robot's Job:** Sort emails into "Spam" or "Not Spam"

- **True Positive:** Correctly catches spam ✅
- **False Positive:** Calls your grandma's email spam ❌ (Bad!)
- **False Negative:** Spam gets into your inbox ❌

**Why F-score?** You want to catch spam BUT not block important emails!

---

### 2. **Online Shopping Reviews** ⭐
**The Robot's Job:** Read reviews and decide "Happy Customer" or "Unhappy Customer"

- **True Positive:** Finds a real happy review ✅
- **False Positive:** Thinks "okay..." means super happy ❌
- **False Negative:** Misses a 5-star review ❌

**Why F-score?** Companies want to know: "How good are we at understanding what customers really feel?"

---

### 3. **Social Media Content Moderation** 🛡️
**The Robot's Job:** Find mean/bullying comments

- **True Positive:** Catches actual bullying ✅
- **False Positive:** Flags friendly jokes as mean ❌ (Annoying!)
- **False Negative:** Misses real bullying ❌ (Dangerous!)

**Why F-score?** Need to catch bad stuff BUT not censor normal conversations!

---

### 4. **Medical Diagnosis Helper** 🏥
**The Robot's Job:** Look at symptoms and say "Sick" or "Healthy"

- **True Positive:** Correctly identifies sick person ✅
- **False Positive:** Says healthy person is sick ❌ (Scary!)
- **False Negative:** Misses sick person ❌ (Very dangerous!)

**Why F-score?** Doctors need accuracy - both catching sick people AND not scaring healthy ones!

---

### 5. **Customer Service Chatbot** 💬
**The Robot's Job:** Decide if customer is "Frustrated" or "Happy"

- **True Positive:** Catches frustrated customer ✅
- **False Positive:** Thinks happy person is mad ❌
- **False Negative:** Misses frustrated customer ❌

**Why F-score?** Need to help upset customers without bothering happy ones!

---

### 6. **Hiring/Resume Screening** 📄
**The Robot's Job:** Find "Good Candidate" resumes

- **True Positive:** Finds qualified person ✅
- **False Positive:** Recommends unqualified person ❌
- **False Negative:** Rejects qualified person ❌ (Lost opportunity!)

**Why F-score?** Companies want to find talent without missing good people!

---

### The Balance Problem

Imagine a security guard at a theme park:

**Too Careful (High Precision, Low Recall):**
- Only lets in people with PERFECT tickets
- Might reject kids with slightly wrinkled tickets
- Park is safe but loses customers 😟

**Too Relaxed (Low Precision, High Recall):**
- Lets everyone in without checking much
- Some people sneak in without tickets
- Lots of customers but security problems 😟

**Just Right (High F1 Score):**
- Checks tickets properly
- Lets in real customers
- Catches ticket cheaters
- Everyone's happy! 😊

---

## Implementation Guide

### The Four Key Metrics

To calculate F-score, you need to track:

1. **True Positives (TP)**: Model says "positive" AND actual is "positive" ✅
2. **False Positives (FP)**: Model says "positive" BUT actual is "negative" ❌
3. **False Negatives (FN)**: Model says "negative" BUT actual is "positive" ❌
4. **True Negatives (TN)**: Model says "negative" AND actual is "negative" ✅

### Step 1: Structure Your CSV

Keep your CSV clean with just test data:

```csv
text,sentiment,__description
"This product is amazing!","positive","Positive: enthusiastic review"
"Terrible experience.","negative","Negative: strong disappointment"
"Best purchase ever!","positive","Positive: strong recommendation"
```

**That's it!** No complex JavaScript in the CSV.

### Step 2: Configure Assertions in YAML

Use `defaultTest` in your config to define assertions once:

```yaml
defaultTest:
  assert:
    # Assertion 1: Accuracy (affects pass/fail)
    - type: javascript
      value: JSON.parse(output).sentiment === context.vars.sentiment
      metric: accuracy

    # Assertion 2: Track true positives (TP)
    - type: javascript
      value: "JSON.parse(output).sentiment === 'positive' && context.vars.sentiment === 'positive' ? 1 : 0"
      metric: true_positives
      weight: 0  # Don't affect pass/fail, just track

    # Assertion 3: Track false positives (FP)
    - type: javascript
      value: "JSON.parse(output).sentiment === 'positive' && context.vars.sentiment === 'negative' ? 1 : 0"
      metric: false_positives
      weight: 0

    # Assertion 4: Track false negatives (FN)
    - type: javascript
      value: "JSON.parse(output).sentiment === 'negative' && context.vars.sentiment === 'positive' ? 1 : 0"
      metric: false_negatives
      weight: 0
```

**Benefits of defaultTest approach:**
- Cleaner CSV (just data, no complex JavaScript)
- Easier to maintain
- Reusable across multiple CSV files
- Define once, apply to all tests

### Step 3: Define Derived Metrics

Add these to your `promptfooconfig.yaml`:

```yaml
derivedMetrics:
  # Precision = TP / (TP + FP)
  # "Of all the things I said were positive, how many actually were?"
  - name: precision
    value: true_positives / (true_positives + false_positives)

  # Recall = TP / (TP + FN)
  # "Of all the things that were positive, how many did I catch?"
  - name: recall
    value: true_positives / (true_positives + false_negatives)

  # F1 Score = 2 * (precision * recall) / (precision + recall)
  # Harmonic mean that balances both precision and recall
  - name: f1_score
    value: 2 * true_positives / (2 * true_positives + false_positives + false_negatives)
```

### Complete Example

#### CSV File (`tests/fscore_simple.csv`)
```csv
text,sentiment,__description
"This product is amazing! I love it!","positive","Positive: enthusiastic review"
"Absolutely terrible experience. Very disappointed.","negative","Negative: strong disappointment"
"Best purchase ever! Highly recommend!","positive","Positive: strong recommendation"
"Waste of money. Do not buy.","negative","Negative: strong warning"
"It's okay, nothing special.","neutral","Neutral: ambiguous sentiment"
"Exceeded all my expectations!","positive","Positive: exceeded expectations"
"Horrible quality, broke after one use.","negative","Negative: quality complaint"
"Great value for the price!","positive","Positive: value statement"
"Not worth it at all.","negative","Negative: not worth it"
"Perfect! Exactly what I needed.","positive","Positive: meets expectations"
```

#### Prompt File (`prompts/sentiment_prompt.txt`)
```
Analyze the sentiment of the following text and respond with ONLY a JSON object in this format:
{"sentiment": "positive" or "negative" or "neutral"}

Text to analyze: {{text}}

Response (JSON only):
```

#### Config File (`promptfooconfig_fscore.yaml`)
```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: "F-Score Classification Example - Sentiment Analysis"

prompts:
  - file://prompts/sentiment_prompt.txt

providers:
  - id: openai:gpt-4o-mini
    config:
      temperature: 0
      response_format:
        type: json_object

tests: file://tests/fscore_simple.csv

derivedMetrics:
  - name: precision
    value: true_positives / (true_positives + false_positives)
  - name: recall
    value: true_positives / (true_positives + false_negatives)
  - name: f1_score
    value: 2 * true_positives / (2 * true_positives + false_positives + false_negatives)

defaultTest:
  assert:
    - type: javascript
      value: JSON.parse(output).sentiment === context.vars.sentiment
      metric: accuracy
    - type: javascript
      value: "JSON.parse(output).sentiment === 'positive' && context.vars.sentiment === 'positive' ? 1 : 0"
      metric: true_positives
      weight: 0
    - type: javascript
      value: "JSON.parse(output).sentiment === 'positive' && context.vars.sentiment === 'negative' ? 1 : 0"
      metric: false_positives
      weight: 0
    - type: javascript
      value: "JSON.parse(output).sentiment === 'negative' && context.vars.sentiment === 'positive' ? 1 : 0"
      metric: false_negatives
      weight: 0
```

### Running the Evaluation

```bash
cd csv-format-example
promptfoo eval -c promptfooconfig_fscore.yaml
promptfoo view
```

### Understanding the Results

After running the evaluation, you'll see:

- **Accuracy**: Overall correctness percentage
- **Precision**: How reliable your positive predictions are
- **Recall**: How well you catch all positive cases
- **F1 Score**: Balanced measure (0 to 1, higher is better)

#### Interpreting Scores

- **High Precision, Low Recall**: Conservative - only flags things when very sure, but misses many
- **Low Precision, High Recall**: Aggressive - catches most cases, but many false alarms
- **High F1 Score**: Good balance between precision and recall

---

## Troubleshooting

### Why Do Assertions "Fail"?

**Common Confusion:** You see assertions returning `0` and think they're failing.

**The Truth:** They're NOT failing - they're **counters**!

#### Example: Positive sentiment test
```
Text: "This is amazing!"
Expected: positive
Output: positive
```

**Results:**
- ✅ Assertion 1 (Accuracy): `true` - PASSES
- ✅ Assertion 2 (True Positive): `1` - Returns 1 (this IS a true positive)
- ✅ Assertion 3 (False Positive): `0` - Returns 0 (this is NOT a false positive)
- ✅ Assertion 4 (False Negative): `0` - Returns 0 (this is NOT a false negative)

**Those 0s are correct!** They mean "this condition doesn't apply."

### Understanding `weight: 0`

```yaml
- type: javascript
  value: "JSON.parse(output).sentiment === 'positive' && context.vars.sentiment === 'positive' ? 1 : 0"
  metric: true_positives
  weight: 0  # ← This is key!
```

**`weight: 0`** means:
- ❌ NOT a pass/fail test
- ✅ JUST counting for statistics
- The test can still PASS even if this returns 0

### What Actually Matters for Pass/Fail

- **Only 1 assertion** (accuracy) determines pass/fail
- **The other 3 assertions** just count metrics for F-score
- **All 4 are necessary** for F-score calculation

**Think of it like a sports game:**
- Assertion 1 (accuracy) = Did you win? (Pass/Fail)
- Assertions 2-4 = Game statistics (points, rebounds, assists)

You need the statistics to understand performance, but only the win/loss matters for the final score!

### Common Issues

#### Issue 1: Accuracy Assertion Failing
**Problem:** `output.sentiment === context.vars.sentiment` returns false

**Solution:** The output is likely a JSON string, not a parsed object. Use:
```javascript
JSON.parse(output).sentiment === context.vars.sentiment
```

#### Issue 2: Duplicate Assertions
**Problem:** Assertions defined in both CSV and defaultTest

**Solution:** Remove assertions from CSV, keep only in defaultTest:
```csv
text,sentiment,__description
"This is great!","positive","Test case"
```

#### Issue 3: All Metrics Show 0
**Problem:** No true positives, false positives, or false negatives being counted

**Solution:** Check that your sentiment values match exactly:
- CSV: `"positive"` and `"negative"`
- Output: `{"sentiment": "positive"}` or `{"sentiment": "negative"}`
- Case-sensitive!

---

## Advanced Topics

### When to Use F-Score

✅ **Use F-score when:**
- Doing classification tasks (sentiment, intent, categories)
- Working with imbalanced datasets
- False positives and false negatives have different costs
- You need both accuracy AND coverage

❌ **Don't use F-score when:**
- Not doing classification
- Simple pass/fail is sufficient
- You only care about one metric (precision OR recall)

### Tips for Best Results

1. **Set weight: 0** for metric-tracking assertions so they don't affect pass/fail
2. **Use defaultTest** instead of CSV assertions for cleaner, more maintainable code
3. **Test with edge cases** including neutral/ambiguous examples
4. **Monitor all metrics** not just F1 - sometimes precision or recall alone is more important
5. **Use temperature: 0** for consistent classification results
6. **Parse JSON output** if your prompt returns JSON format

### F-Score Variations

- **F0.5 Score**: Weights precision higher than recall
- **F2 Score**: Weights recall higher than precision
- **F1 Score**: Equal weight to precision and recall (most common)

### Multi-Class Classification

For more than 2 classes (positive/negative/neutral), you can:
- Calculate F-score per class
- Use macro-averaging (average of all class F-scores)
- Use micro-averaging (calculate from total TP, FP, FN)

---

## Summary

### Key Takeaways

1. **JavaScript assertions are counters** that watch the AI and count different types of right and wrong answers.

2. **F-score tells us if the AI is both careful (precision) and thorough (recall)** - not just one or the other.

3. **It's used everywhere today** - from email spam filters to medical diagnosis - anywhere we need an AI to sort things correctly without making too many mistakes or missing too many things.

4. **Only one assertion affects pass/fail** - the others (with `weight: 0`) are just for statistics.

5. **Clean CSV + defaultTest** is the best approach for maintainability.

### The Takeaway

Just like teaching a kid to clean their room:
- **Precision** = Puts toys in RIGHT boxes (not messy)
- **Recall** = Finds ALL the toys (doesn't leave any under the bed)
- **F1 Score** = Both clean AND thorough! ⭐

The JavaScript code is just a fancy way to keep score automatically!

---

## References

- [Promptfoo F-Score Documentation](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/#f-score)
- [Promptfoo CSV Format Documentation](https://www.promptfoo.dev/docs/configuration/test-cases/#csv-format)
- [Wikipedia: F-score](https://en.wikipedia.org/wiki/F-score)
- [Understanding Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall)
