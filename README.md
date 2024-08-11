# InfoAssist Bot

InfoAssist Bot streamlines the retrieval of frequently asked questions in the workplace, allowing employees to quickly access necessary information without consulting senior staff or colleagues. Housed within a Docker container, it is scalable and maintainable across different infrastructures.

**Currently in use at the ONGC BKC office**, InfoAssist Bot provides quick answers to common queries, enhancing operational efficiency and productivity.

## Features

1. **User-Friendly Interface**:
   - Intuitive and straightforward, requiring no specialized training.

2. **Dynamic Question Assistance**:
   - Provides relevant answers and displays similar questions to broaden assistance.

3. **Admin Portal for Data Management**:
   - Backend access for adding, updating, or deleting questions and answers.

4. **Modular and Scalable Code**:
   - Easily modifiable and expandable, with Docker-based deployment for scalability.

5. **Use of Docker for Scalability and Load Balancing**:
   - Can be scaled horizontally across multiple servers for efficient handling of high user volume.

6. **Open Source Technology**:
   - Customizable and integrable with existing systems or third-party services.

## Installation

### Prerequisites
**Docker**: Download from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Setup Instructions

#### Step 1: Obtain the Project
```bash
git clone https://github.com/abhay702/InfoAssist.git
cd InfoAssist
```
Alternatively, download and extract the project files into a directory.

#### Step 2: Configuration (Optional)
- Navigate to the project directory.
- Open the `.env` file to set necessary environment variables.

#### Step 3: Build the Docker Container
```bash
docker-compose build
```

#### Step 4: Run the Docker Container
```bash
docker-compose up -d
```

#### Step 5: Verify the Installation
- Navigate to `http://localhost:5000` or the configured `HOST` and `PORT`.

#### Step 6: Admin Setup
- Log in with admin credentials to add or modify data.

### Troubleshooting
- Obtain container details:
  ```bash
  docker ps -a
  docker inspect <container_id>
  ```
  
- Check Docker container logs for errors:
  ```bash
  docker logs <container_name>
  ```


## Usage

### Accessing the Chatbot
1. **Web Interface**: Navigate to `http://<Host-IP-Address>:5000`.

2. **Chat Interface**: Click on the chat icon to start interacting with the bot.

### Interacting with the Chatbot
1. **Starting a Session**: Type your question and press enter or click send.
2. **Receiving Answers**: The bot processes and returns the most relevant answer, suggesting similar questions if needed.

### Admin Features
1. **Login**: Access the admin page from the homepage to manage questions and answers.
2. **Adding Data**: Add new questions and answers to keep the bot updated.
3. **Retraining**: Retrain the bot periodically to incorporate new data.

## Screenshots

![screen-recorder-fri-jul-19-2024-23-19-21-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/0cdd2ba2-fcc7-44ce-8a27-b652cc15a6c6)

![image](https://github.com/user-attachments/assets/ce1315e1-c583-4220-9f84-eab41f96d219)
![image](https://github.com/user-attachments/assets/71cd82f2-54c2-4836-8def-52a8fc1ab148)

## References

1. **Hugging Face Models**: For semantic search capabilities, the chatbot uses the all-MiniLM-L6-v2 model. More details are available at [Hugging Face](https://huggingface.co/).
2. **Docker Documentation**: Detailed in the [Docker Official Documentation](https://docs.docker.com/).
3. **Flask Documentation**: Described in the [Flask Documentation](https://flask.palletsprojects.com/).
4. **Gunicorn Documentation**: Running the Flask application in production, as outlined in the [Gunicorn Official Documentation](https://gunicorn.org/).
