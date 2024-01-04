```javascript
import React from 'react';

class PromptGenerator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      theme: '',
      emotion: '',
      genre: '',
      prompt: '',
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    // Here you would call the OpenAI API to generate a prompt based on the state variables
    // For now, we'll just set the prompt to a static string
    this.setState({prompt: 'This is your creative prompt!'});
  }

  render() {
    return (
      <div className="PromptGenerator">
        <h2>Prompt Generator</h2>
        <form onSubmit={this.handleSubmit}>
          <label>
            Theme:
            <input type="text" name="theme" value={this.state.theme} onChange={this.handleChange} />
          </label>
          <label>
            Emotion:
            <input type="text" name="emotion" value={this.state.emotion} onChange={this.handleChange} />
          </label>
          <label>
            Genre:
            <input type="text" name="genre" value={this.state.genre} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Generate Prompt" />
        </form>
        <p>{this.state.prompt}</p>
      </div>
    );
  }
}

export default PromptGenerator;
```
