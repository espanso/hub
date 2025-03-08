# LLM Prompts Package for Espanso

This package provides a collection of useful prompt templates for Large Language Models (LLMs) like ChatGPT, Claude, and others. It allows you to quickly insert well-structured prompts into any text field using Espanso's text expansion capabilities.

## Installation

This package is designed for [Espanso](https://espanso.org/), a cross-platform text expander.

If you already have Espanso installed, you can install this package with:

```bash
espanso install llm-prompts
```

## Usage

You can use these prompts in two ways:

1. Type `:prompt` to open a search menu with all available prompts
2. Use the specific trigger for each prompt directly (e.g., `:rtf`, `:bab`)

After inserting a prompt template, fill in the details as needed. The cursor will be positioned at the first input field.

## Available Prompts

### Simple Prompts

- `:pirate` - "Speak like a pirate."
- `:helpful` - "You are a helpful assistant."

### Structured Frameworks

#### Role-Task-Format (`:rtf`)
A framework to clearly define the role the AI should assume, the task it should perform, and the format of the response.

```
Role: 
Task: 
Format:
```

Source: [LinkedIn post by Jeremy Grandillon](https://www.linkedin.com/posts/jeremygrandillon_5-chatgpt-prompt-frameworks-that-make-your-activity-7301956962898837504-NR_i)

#### Before-After-Bridge (`:bab`)
A framework to describe the current state, desired outcome, and steps to get there.

```
Before: 
After:
Bridge: outline the steps or actions to bridge the gap.
```

Source: [LinkedIn post by Jeremy Grandillon](https://www.linkedin.com/posts/jeremygrandillon_5-chatgpt-prompt-frameworks-that-make-your-activity-7301956962898837504-NR_i)

#### Situation-Complication-Question-Answer (`:scqa`)
A problem-solving framework that provides context, identifies complications, poses a question, and seeks an answer.

```
Situation: 
Complication:
Question:
Answer: 
```

Source: [LinkedIn post by Jeremy Grandillon](https://www.linkedin.com/posts/jeremygrandillon_5-chatgpt-prompt-frameworks-that-make-your-activity-7301956962898837504-NR_i)

### Special Purpose Prompts

#### Goal Setting (`:goals`)
A prompt designed to help you set more ambitious goals through a series of challenging questions.

Source: [Forbes article by Jodie Cook](https://www.forbes.com/sites/jodiecook/2024/07/23/5-chatgpt-prompt-frameworks-to-accelerate-your-success-make-leapfrog-moves/)

#### Abundance Mindset Quiz (`:abundance`)
A comprehensive prompt that:
1. Creates an 8-question quiz to assess your mindset
2. Analyzes your responses
3. Provides suggestions to develop a more abundant mindset

Source: [Forbes article by Jodie Cook](https://www.forbes.com/sites/jodiecook/2024/07/23/5-chatgpt-prompt-frameworks-to-accelerate-your-success-make-leapfrog-moves/) (modified)

#### Startup Investor (`:startup`)
A prompt that makes the AI act as a startup angel investor to:
1. Analyze potential startup pitches
2. Provide feedback on market potential, scalability, competitive landscape, and team competence
3. Score each factor out of 10
4. Conclude with investment recommendation

Source: [GitHub Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts/pull/828)

## Contributing

Feel free to suggest additional prompt frameworks or improvements to existing ones by opening an issue or pull request.

## License

This package is available under the MIT License.
