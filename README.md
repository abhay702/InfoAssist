
# InfoAssist Bot



InfoAssist Bot is designed to simplify the retrieval of frequently asked questions in the workplace, allowing employees to access necessary information swiftly without needing to consult senior staff or colleagues. This bot is housed within a Docker container, making it highly scalable and maintainable across different infrastructures.

**Currently in use at the ONGC BKC office**, InfoAssist Bot aids employees by providing quick answers to common queries, helping to streamline operations and maintain productivity without the complexities of traditional communication barriers. This practical implementation highlights the bot's functionality and adaptability within a professional setting.


## Features



InfoAssist Bot is designed to provide a robust and user-friendly interface for employees seeking quick answers to their questions. Below are the key features that make InfoAssist Bot an essential tool for workplace efficiency:

1. **User-Friendly Interface**:
   - The bot features a straightforward and intuitive interface, allowing users to interact with it without any specialized training. This simplicity ensures that all employees can effectively utilize the bot to access the information they need.

2. **Dynamic Question Assistance**:
   - When users search for information, the bot not only provides the most relevant answer but also displays similar questions. This feature is particularly useful if the user's initial query does not exactly match the content in the database, thereby broadening the scope of assistance without additional user effort.

3. **Admin Portal for Data Management**:
   - An admin login feature facilitates backend access where new questions and answers can be added, and existing content can be updated or deleted. This ensures that the bot’s database remains up-to-date with the latest information and organizational changes.

4. **Modular and Scalable Code**:
   - The bot is built on modular code, making it easy to modify or expand its capabilities. Its Docker-based deployment allows for easy scalability, ensuring that the bot can handle increased loads, making it ideal for organizations of any size.

5. **Use of Docker for Scalability and Load Balancing**:
   - Leveraging Docker technology, the bot can be scaled horizontally across multiple servers to handle high user volume efficiently. This scalability ensures reliable performance and availability, even during peak usage times.

6. **Open Source Technology**:
   - Employing an open-source model enhances the flexibility and adaptability of the bot. Organizations can customize the bot according to their specific needs and integrate it with existing systems or third-party services.


## Installation

**Installation Instructions for InfoAssist Bot**

Below are the detailed instructions to set up and run the InfoAssist Bot within your environment. These steps assume that you have basic knowledge of command-line operations and access to a system with Docker installed.

### Prerequisites
 **Docker** : Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).


### Setup Instructions

#### Step 1: Obtain the Project
- If available from a GitHub repository:
  ```bash
  git clone https://github.com/abhay702/InfoAssist.git
  cd InfoAssist
  ```
- Alternatively, download and extract the project files into a directory of your choice.

#### Step 2: Configuration (Optional)
The project shall fucntion with all the default settings if there are no discrepancies.
- Navigate to the project directory.
- Open the `.env` file or any other configuration files provided to set the necessary environment variables like `PORT`, `HOST`, etc.
- Update the settings according to your system and requirements.

#### Step 3: Build the Docker Container
- From the command line, run the following command in the project directory to build the Docker image:
  ```bash
  docker-compose build
  ```

#### Step 4: Run the Docker Container
- After successfully building the image, you can start the service using:
  ```bash
  docker-compose up -d
  ```
- This command will start the bot in a detached mode.

#### Step 5: Verify the Installation
- Open your web browser and navigate to `http://localhost:5000` or whatever `HOST` and `PORT` you have configured. You should see the bot's interface.
- Try interacting with the bot to ensure it is responding as expected.

#### Step 6: Admin Setup
- If your bot has an administrative interface to add or modify data, log in with the credentials provided or set up during the configuration step.
- Test adding a new FAQ to verify that the admin functionalities are working correctly.

### Troubleshooting
- If the bot does not start, check the Docker container logs for any errors:
  ```bash
  docker logs <container_name>
  ```
- To obtain the container ID and other details, use:
  ```bash
  docker ps -a
  ```
- For detailed inspection of a container, use:
  ```bash
  docker inspect <container_id>
  ```
- Ensure all environment variables are set correctly and that the Docker environment has sufficient resources.
- If you encounter network issues, verify the Docker network settings or consult Docker’s network documentation for troubleshooting tips.

## Usage

**Accessing the Chatbot:**
1. **Web Interface**: Once the chatbot application is running, you can access it through a web browser by navigating to `http://<Host-IP-Address>:5000`. Replace `<Host-IP-Address>` with the IP address of the host machine where the Docker container is running.
This can also be given custom names, by using a reverse proxy, if the container if deployed on the web, it can be accessed by putting the name of the website.

2. **Chat Interface**: Upon accessing the chatbot via the web interface, you will be greeted by the homepage. Click on the chat icon to start interacting with the chatbot.


**Interacting with the Chatbot:**
1. **Starting a Session**: Simply type your question in the message box and press enter or click the send button. The chatbot is designed to understand natural language queries related to common FAQs within your organization.

2. **Receiving Answers**: After submitting your question, the chatbot will process it and return the most relevant answer. If the exact answer is not found, the chatbot may suggest similar questions to ensure you find the information you need.

3. **Navigation**: Use the navigation menu to access different sections of the chatbot, such as the Admin panel (if you have admin rights), where new data can be added to the chatbot's knowledge base.

**Admin Features:**
1. **Login**: If you are an administrator, you can log in through the admin page accessible from the homepage. This area allows you to manage the questions and answers that the chatbot uses to respond to inquiries.

2. **Adding Data**: Within the admin panel, you can add new questions and their corresponding answers to enhance the chatbot's functionality. This ensures the chatbot remains up-to-date with the latest information and organizational changes.

3. **Retraining**: Periodically, you may need to retrain the chatbot to incorporate all the new data added through the admin panel. This ensures that the chatbot continually improves and adapts to new information.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## References 





1. **Hugging Face Models**: For semantic search capabilities, the chatbot utilizes the all-MiniLM-L6-v2 model. More details are available at [Hugging Face](https://huggingface.co/).

2. **Docker Documentation**: Information on Docker, used for deployment and scalability of the chatbot, is detailed in the [Docker Official Documentation](https://docs.docker.com/).

3. **Flask Documentation**: The web framework for creating the chatbot's interface is described in the [Flask Documentation](https://flask.palletsprojects.com/).

4. **Gunicorn Documentation**: Gunicorn is employed to run the Flask application in production, as outlined in the [Gunicorn Official Documentation](https://gunicorn.org/).

