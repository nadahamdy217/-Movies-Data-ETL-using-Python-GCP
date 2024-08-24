# 🎥 ETL Movies Data Project

## **🚀 Project Overview**

Welcome to the ETL Movies Data Project! 🌟 This project is a deep dive into building an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Docker, and a Google Cloud Pub/Sub emulator. We’re working with a dataset of movie ratings, transforming it into a format that's ready for analysis, and loading it into a Docker container for easy access and management. This project is perfect for those looking to simulate a real-world ETL process in a local environment. 💻

---

## **🗂 Project Structure**

Here’s how our project is organized:

### `ETL_MOVIES/`
- **`data/`**                           # Where all the magic data lives! 🎩
  - **`ratings.csv`**                 # Contains rated movie data 📊
  - **`movies.csv`**                  # Contains information about movies 🎥
  - **`full_data.csv`**               # The preprocessed movie data file 🗃

- **`Dockerfile`**                    # Our recipe for the Docker environment 📦

- **`requirements.txt`**              # All the ingredients (dependencies) 🛠

- **`README.md`**                     # This very guide you’re reading! 📚

- **`Scripts/`**                      # Scripts to automate various tasks 🎛
  - **`setup_env.bat`**               # Environment setup script ⚙️
  - **`download_data.bat`**           # Data download script ⬇️
  - **`start_emulator.py`**           # Start the Pub/Sub emulator 🚀
  - **`create_topic_subscription.py`** # Create Pub/Sub topic and subscription 📝
  - **`publish_test_message.py`**     # Test data ingestion 🧪
  - **`process_data.py`**             # Extract CSV files 📂
  - **`preprocessing_data.py`**       # Clean up the data 🧼
  - **`publish_data.py`**             # Publish data to the container 🚚

Feel free to explore each part of the project to understand its role and how everything fits together. Happy coding! 👩‍💻👨‍💻


## **🔧 Tools and Technologies**

- **Python** 🐍: The core language for our scripts.
- **Docker** 🐳: To containerize and run everything smoothly.
- **Google Cloud Pub/Sub** ☁️: For simulating real-time data streaming.
- **Pandas** 🐼: Our go-to for data manipulation.
- **Windows Batch Scripting** 🖥: Automating the setup and downloads.
- **Google Cloud SDK** 🌐: For interacting with Google Cloud services.

---

## **📋 Environment Setup**

Ready to get started? Here’s what you need to do:

1. **Install Required Tools:**
   - Docker Desktop
   - Python 3.12.5
   - Google Cloud SDK

2. **Clone the Repository:**
   - Use Git to clone the repository and dive into the project directory.

3. **Install Python Dependencies:**
   - Create a virtual environment and install dependencies with a flick of a command.

---

## **📚 Project Steps**

Here’s a step-by-step guide to get you through the project:

### **1️⃣ Setup Environment**

**Goal:** Set up the project environment with all the necessary dependencies.

**How:** Run the `setup_env.bat` script, and let the automation magic happen! ✨

---

### **2️⃣ Download Data**

**Goal:** Get the movie ratings data.

**How:** Simply run `download_data.bat`, and the data will be at your service! 📥

---

### **3️⃣ Set Up Pub/Sub Emulator**

**Goal:** Simulate the Pub/Sub environment locally.

**How:** Kickstart the emulator with `start_emulator.py`. 🚀

---

### **4️⃣ Build Docker Image**

**Goal:** Package everything into a Docker image.

**How:** Build the image using Docker, and watch it come to life! 🛠

---

### **5️⃣ Run Docker Container**

**Goal:** Spin up the Docker container.

**How:** Use the Docker run command, and let the container do its thing. 🏃‍♂️

---

### **6️⃣ Create Pub/Sub Topic and Subscription**

**Goal:** Create a Pub/Sub topic and subscription.

**How:** Execute `create_topic_subscription.py`, and set the stage for data flow. 🌐

---

### **7️⃣ Test Data Ingestion**

**Goal:** Ensure data ingestion works smoothly.

**How:** Run `publish_test_message.py` and see the messages flow! 🎯

---

### **8️⃣ Extract CSV Files**

**Goal:** Extract and prepare the data.

**How:** Run `process_data.py` and get your CSVs ready for action! 📑

---

### **9️⃣ Preprocess Data**

**Goal:** Clean and prep the data.

**How:** Execute `preprocessing_data.py`, and your data will be spotless! 🧼
- inside this Python file:
  - null values have been filled
  - datatype correction
  - merge data depending on the item_id

---

### **🔟 Create Folder in Docker Container**

**Goal:** Create a place in the container for our data.

**How:** Access the Docker terminal and create the `/data` folder. 📂

---

### **1️⃣1️⃣ Publish Data to Container**

**Goal:** Send the data into the Docker container.

**How:** Run `publish_data.py` and watch the data transfer! 🚚

---

## **💡 Understanding Pub/Sub and Its Role**

Google Cloud Pub/Sub is all about handling data in real-time, and this project, allows us to simulate how large-scale data processing would work in the cloud. The Pub/Sub emulator lets us develop and test everything locally, so we’re ready for the real cloud when the time comes. ☁️

---

## **🚧 Challenges Faced**

- **Handling Big Data:** Processing 100,000 rows was a challenge, but we conquered it! 💪
- **Local Cloud Simulation:** Setting up the Pub/Sub emulator wasn’t easy, but it was worth it. 🎓
- **Data Cleaning:** Ensuring clean and reliable data required some serious attention to detail. 🧹

---

## ** ⭐ Result**

![image](https://github.com/user-attachments/assets/736f8cd2-bab3-4306-8e24-a3d266961f41)


---

## **🎉 Conclusion**

This project is a full demonstration of how to build a robust ETL pipeline, complete with Dockerization and cloud simulations. Whether you’re here to learn or to build, this project has all the tools and guidance you need. Happy coding! 👩‍💻👨‍💻



---

## **📂 Repository**

Find everything you need in our [GitHub repository](https://github.com/nadahamdy217/Movies-Data-ETL-using-Python-GCP/tree/main). Dive in, explore, and feel free to contribute! 🎁

---

## **Contributing**

We welcome contributions to this project! If you’d like to contribute or have any questions, please contact:

- **Author:** [Nada Hamdy Fatehy]
- **Email:** nadahamdy2172002@gmail.com
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/nada-hamdy-2265692a3/)
- **GitHub:** [GitHub](https://github.com/nadahamdy217)

