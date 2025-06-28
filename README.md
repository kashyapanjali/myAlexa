# Ask Anjali - Voice Assistant

A web-based voice assistant that uses speech recognition and OpenAI's GPT to answer questions.

## Features

- Voice input using browser's Speech Recognition API
- AI-powered responses using OpenAI GPT-3.5-turbo
- Text-to-speech output using browser's Speech Synthesis API
- Web-based interface - no installation required
- Modern, responsive UI

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up OpenAI API Key**
   
   **Option 1: Environment Variable (Recommended)**
   ```bash
   # On Windows
   set OPENAI_API_KEY=your_actual_api_key_here
   
   # On macOS/Linux
   export OPENAI_API_KEY=your_actual_api_key_here
   ```
   
   **Option 2: Direct in code (Not recommended for production)**
   Edit `app.py` and replace `"your_api_key_here"` with your actual OpenAI API key.

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open in Browser**
   Navigate to `http://localhost:5000`

## How to Use

1. Click the microphone button (🎤)
2. Allow microphone permissions when prompted
3. Speak your question clearly
4. Wait for the AI response
5. The response will be displayed and spoken back to you

## Browser Compatibility

- **Chrome/Edge**: Full support for speech recognition and synthesis
- **Firefox**: Limited support, may not work properly
- **Safari**: Limited support, may not work properly

## Troubleshooting

### Speech Recognition Issues
- Make sure you're using Chrome or Edge
- Allow microphone permissions when prompted
- Check that your microphone is working
- Try refreshing the page if recognition stops working

### Speech Synthesis Issues
- Check that your system volume is turned on
- Some browsers may block autoplay - try clicking the page first
- Speech synthesis may be disabled in your browser settings

### API Errors
- Verify your OpenAI API key is correct
- Check your internet connection
- Ensure you have sufficient API credits

## Files Structure

```
myAlexa/
├── app.py              # Flask backend server
├── main.py             # Alternative desktop implementation
├── requirements.txt    # Python dependencies
├── static/
│   ├── script.js       # Frontend JavaScript
│   └── style.css       # Styling
└── templates/
    └── index.html      # Main HTML page
```

## Notes

- The application requires an active internet connection for OpenAI API calls
- Speech recognition works best in quiet environments
- For production use, consider using environment variables for API keys
- The desktop version (`main.py`) is a separate implementation using different libraries 