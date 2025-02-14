<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temperature Box</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            position: relative;
        }
        .temperature-box {
            width: 220px;
            height: 120px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 26px;
            font-weight: bold;
            border-radius: 12px;
            transition: background-color 0.5s;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            background-color: white;
        }
        .heading {
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 20px;
            font-weight: bold;
        }
        .button-container {
            margin-top: 20px;
        }
        button {
            padding: 12px;
            font-size: 16px;
            margin: 5px;
            cursor: pointer;
            border: none;
            border-radius: 6px;
            background-color: #ff5e62;
            color: white;
            font-weight: bold;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        button:hover {
            background-color: #ff3b3f;
        }
        .emoji {
            font-size: 30px;
        }
    </style>
</head>
<body>
    <div class="heading"> <h1> 🍅 Vegetable: Tomato 🍅</h1></div>
    <h1>SET TEMPERATURE</h1>
    <div class="temperature-box" id="tempBox">Loading...</div>
    <div class="button-container">
        <button onclick="increaseTemperature()">Increase Temperature 🔼</button>
        <button onclick="decreaseTemperature()">Decrease Temperature 🔽</button>
    </div>
    
    <h2>Cold Storage Temperature</h2>
    <div class="temperature-box" id="coldStorageTemp">Loading...</div>

    <script>
        let temperature = 18;

        function updateTemperatureDisplay() {
            let tempBox = document.getElementById('tempBox');
            tempBox.textContent = "🍅 " + temperature + "°C 🍅";
            
            if (temperature < 15) {
                tempBox.style.backgroundColor = "lightblue";
            } else if (temperature <= 22) {
                tempBox.style.backgroundColor = "lightgreen";
            } else {
                tempBox.style.backgroundColor = "tomato";
            }
        }

        function increaseTemperature() {
            if (temperature < 23) {
                temperature++;
                updateTemperatureDisplay();
            } else {
                alert("It is not an ideal temperature for tomatoes 🍅");
            }
        }

        function decreaseTemperature() {
            if (temperature > 13) {
                temperature--;
                updateTemperatureDisplay();
            } else {
                alert("It is not an ideal temperature for tomatoes 🍅");
            }
        }

        function updateColdStorageTemperature() {
            let coldStorageTempBox = document.getElementById('coldStorageTemp');
            let randomTemp = (Math.random() * (31 - 27) + 27).toFixed(2);
            coldStorageTempBox.textContent = "❄️ " + randomTemp + "°C ❄️";
        }

        updateTemperatureDisplay();
        updateColdStorageTemperature();
        setInterval(updateColdStorageTemperature, 3000);
    </script>
</body>
</html>
