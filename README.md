# Weather Application 🌤️

A simple yet elegant web application built with Flask that provides real-time weather information for any city worldwide using the OpenWeatherMap API.

## 📖 Project Overview

This weather application allows users to:
- **Search for current weather conditions** by entering any city name
- **View detailed weather information** including temperature, weather description, and "feels like" temperature
- **Experience a clean, responsive user interface** with dark theme styling
- **Handle invalid city names** gracefully with proper error messaging

The application is perfect for quickly checking weather conditions and serves as an excellent example of integrating external APIs with a Flask web application.

## ✨ Key Features

- 🌍 **Global Weather Data**: Get weather information for cities worldwide
- 🎨 **Modern UI**: Clean, dark-themed interface with responsive design
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- ⚡ **Fast & Lightweight**: Minimal dependencies for quick loading
- 🛡️ **Error Handling**: Graceful handling of invalid city names
- 🌡️ **Metric System**: Temperature displayed in Celsius with "feels like" information

## 🛠️ Technologies & Dependencies

### Backend Technologies
- **Python 3.x** - Programming language
- **Flask 3.1.1** - Lightweight web framework
- **Waitress 3.0.2** - Production-ready WSGI server
- **Requests 2.32.4** - HTTP library for API calls
- **python-dotenv 1.1.1** - Environment variable management

### Frontend Technologies
- **HTML5** - Markup language
- **CSS3** - Styling with modern flexbox layout
- **Jinja2 3.1.6** - Template engine (comes with Flask)

### External API
- **OpenWeatherMap API** - Weather data provider

### Additional Dependencies
- **blinker 1.9.0** - Signal support for Flask
- **certifi 2025.6.15** - Certificate validation
- **charset-normalizer 3.4.2** - Character encoding detection
- **click 8.2.1** - Command line interface utilities
- **idna 3.10** - Internationalized domain names
- **itsdangerous 2.2.0** - Data signing utilities
- **MarkupSafe 3.0.2** - Template string safety
- **urllib3 2.5.0** - HTTP client
- **Werkzeug 3.1.3** - WSGI utilities

## 📁 Project Structure

```
Final-project/
│
├── Backend/
│   ├── server.py              # Main Flask application server
│   └── weather.py             # Weather API integration module
│
├── static/
│   └── styles/
│       └── style.css          # Application styling
│
├── templates/
│   ├── index.html             # Home page template
│   ├── weather.html           # Weather results template
│   └── city-not-found.html    # Error page template
│
├── __pycache__/               # Python cache files
│   └── weather.cpython-312.pyc
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

### File Descriptions

- **`Backend/server.py`**: Main Flask application with route handlers for home page, weather data retrieval, and error handling
- **`Backend/weather.py`**: Contains the `get_current_weather()` function that interfaces with the OpenWeatherMap API
- **`static/styles/style.css`**: CSS styling for the entire application with dark theme and responsive design
- **`templates/index.html`**: Landing page with city input form
- **`templates/weather.html`**: Displays weather information for the requested city
- **`templates/city-not-found.html`**: Error page shown when an invalid city is entered
- **`requirements.txt`**: List of all Python package dependencies

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.7+** installed on your system
- **Git** for cloning the repository
- **OpenWeatherMap API Key** (free registration required)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Abdelrahman-Yasser-Zakaria/weather-app.git
cd Final-project
```

### Step 2: Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv weather_app_env

# Activate virtual environment
# On Linux/Mac:
source weather_app_env/bin/activate
# On Windows:
weather_app_env\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

1. **Get an API Key**:
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key

2. **Create Environment File**:
   ```bash
   # Create .env file in the project root
   touch .env
   ```

3. **Add Your API Key**:
   ```env
   OpenWeather_API_KEY=your_api_key_here
   ```

### Step 5: Run the Application

#### Development Mode
```bash
cd Backend
python server.py
```

#### Production Mode (using Waitress)
The application is configured to run with Waitress server by default:
```bash
cd Backend
python server.py
```

The application will be available at: **http://localhost:8000**

## 🎯 Usage Instructions

1. **Access the Application**: Open your web browser and navigate to `http://localhost:8000`

2. **Search for Weather**: 
   - Enter any city name in the search box
   - Click "Submit" or press Enter

3. **View Results**:
   - **Valid city**: See current temperature, weather description, and "feels like" temperature
   - **Invalid city**: Receive a "City not found" message with option to try again

4. **Search Again**: Use the search form on any page to look up weather for different cities

## 🔧 Configuration

### Default Settings
- **Server Host**: `0.0.0.0` (accessible from any network interface)
- **Server Port**: `8000`
- **Default City**: `Cairo` (used when no city is specified)
- **Temperature Units**: Metric (Celsius)

### Customization Options
- **Change default city**: Modify the default value in `server.py` and `weather.py`
- **Change temperature units**: Update the `units` parameter in the API URL (options: `metric`, `imperial`, `kelvin`)
- **Modify styling**: Edit `static/styles/style.css` to customize the appearance
- **Change port**: Update the `port` parameter in the `serve()` function

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError"**: Ensure all dependencies are installed with `pip install -r requirements.txt`

2. **API Key Errors**: 
   - Verify your API key is correctly set in the `.env` file
   - Ensure your OpenWeatherMap API key is active (can take a few minutes after registration)

3. **Port Already in Use**: 
   - Change the port number in `server.py`
   - Or kill the process using the port: `sudo lsof -t -i tcp:8000 | xargs kill -9`

4. **City Not Found**: 
   - Check spelling of city name
   - Try using city name with country code (e.g., "London, UK")

## 🌟 Future Enhancements

- 📅 5-day weather forecast
- 🗺️ Interactive weather maps
- 📊 Weather charts and graphs
- 🌓 Light/dark theme toggle
- 📱 Progressive Web App (PWA) features
- 🔄 Auto-refresh functionality
- 📍 Geolocation-based weather detection

---
