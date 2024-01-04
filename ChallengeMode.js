```javascript
import React from 'react';

class ChallengeMode extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      challenge: '',
    };

    this.handleGenerateChallenge = this.handleGenerateChallenge.bind(this);
  }

  handleGenerateChallenge() {
    // Here you would call the OpenAI API to generate a daily challenge
    // For now, we'll just set the challenge to a static string
    this.setState({challenge: 'This is your daily creative challenge!'});
  }

  componentDidMount() {
    // Generate a new challenge when the component mounts
    this.handleGenerateChallenge();
  }

  render() {
    return (
      <div className="ChallengeMode">
        <h2>Creative Challenge Mode</h2>
        <button onClick={this.handleGenerateChallenge}>Generate New Challenge</button>
        <p>{this.state.challenge}</p>
      </div>
    );
  }
}

export default ChallengeMode;
```
