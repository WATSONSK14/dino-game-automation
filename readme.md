# **Dino Bot – Chrome Dino Game Automation**

---

## 🧪 Description
This project automates the Chrome Dino game using Python.  
It detects obstacles (cactus and birds) in real-time and reacts accordingly by jumping or ducking.  
The bot achieves over **95% success rate** in obstacle detection and response.
---

## 🧰 Technologies Used
- **Python**
- **PIL (ImageGrab)** – for screen capture and pixel analysis  
- **PyAutoGUI** – for keyboard control  
- **Time** – for delay and timing logic

---
## 🧠 Features
- Real-time obstacle detection using pixel color analysis  
- Dual-mode detection: **day/night** color support  
- Separate detection zones for cactus and birds  
- Jump (`space`) and duck (`down`) behavior  
- Modular and readable code structure  
- Adjustable detection box coordinates for screen calibration

---

## 🧪 How It Works
```python
# Detect cactus
cactus = ImageGrab.grab(bbox=(223, 725, 240, 735))

# Detect bird
bird = ImageGrab.grab(bbox=(223 , 585, 240, 633 ))

# Check pixel colors
if r == 83 and g == 83 and b == 83:
    # Day mode detection
elif r == 172 and g == 172 and b == 172:
    # Night mode detection
```
---
## 🚀 Usage
1. Open Chrome [Dino Game](https://elgoog.im/dinosaur-game/) 
2. Run the script 
3. Bot will automatically jump or duck based on obstacle detection
4. Press (`Ctrl+C`) to stop

---
## 📈 Success Rate
* Obstacle detection: ~95%
* Night/day mode supported
* Only minor misses during fast transitions
---

## 📁 Project Status
✅ Jump logic complete  
✅ Duck logic implemented  
✅ Dual-color detection working  
🟡 Final polish on duck timing (optional)  

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

Created by **WATSONSK14**  
- GitHub: [github.com/WATSONSK14](https://github.com/WATSONSK14)
