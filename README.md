# ChefMate: Restaurant Clustering & Cooking Guide Application

## ***Overview***
**ChefMate** is an intelligent web application designed to enhance dining and cooking experiences. It recommends restaurants based on user preferences and integrates a chef-like chatbot assistant to guide users in preparing recipes. This project leverages machine learning, cloud computing, and an interactive user interface to deliver personalized solutions.

---

## ***Features***
- **Restaurant Recommendations**: Personalized suggestions based on user preferences, cuisines, or dishes.
- **Dynamic Data Visualizations**: Interactive maps, ratings, and metrics for restaurant insights.
- **Recipe Chatbot**: Real-time guidance for cooking instructions.
- **Cloud Integration**: AWS services for scalable data storage, preprocessing, and application hosting.

---

## ***Skills Acquired***
- Streamlit application development
- Machine learning (clustering) model training
- AWS services: S3, RDS, EC2
- Data cleaning and preprocessing
- ML model integration with applications
- Chatbot integration using conversational AI
- Dynamic user interface development

---

## ***Domains***
- Food and Beverages
- Machine Learning & AI
- Cloud Computing

---

## ***Problem Statement***
Develop an application that clusters and recommends restaurants based on user inputs, such as preferred cuisine or dishes, while providing a chatbot assistant for recipe guidance.

---

## ***Technical Approach***
- **Data Storage**:
  - Collected raw data in **JSON format** containing restaurant and recipe details from the Zomato dataset.
  - Uploaded the raw data to an **AWS S3 bucket** for scalable and secure storage.
  - Ensured proper folder structure in S3 to separate restaurant data from recipe data for better manageability.

- **Data Cleaning and Preprocessing**:
  - Pulled raw data from AWS S3 into a local environment for preprocessing.
  - Handled missing or inconsistent values, such as null ratings or incomplete location details.
  - Converted JSON data into structured formats (pandas DataFrames) for easier manipulation.
  - Extracted relevant features (e.g., Cuisine, Ratings, Longitude, Latitude) essential for clustering and recommendations.
  - Normalized numeric features and encoded categorical variables using one-hot encoding to prepare data for model training.

- **Database Management**:
  - Designed relational database schemas for storing cleaned and preprocessed data.
  - Uploaded the cleaned data to **AWS RDS (Relational Database Service)** for efficient querying and integration with the application.
  - Structured tables to include entities such as Restaurant Info, Cuisine Types, and Ratings for seamless access.

- **Model Training and Evaluation**:
  - Experimented with three clustering algorithms:
    - **K-Means**
    - **Hierarchical Clustering**
    - **Gaussian Mixture Model (GMM)**
  - Calculated **Silhouette Score** and **Calinski-Harabasz Score** for model evaluation and comparison.
  - Selected **K-Means** as the best model due to its superior performance:
    - **Silhouette Score**: 0.912553
    - **Calinski-Harabasz Score**: 750248.478826
  - Stored the trained **K-Means model** in the application directory for real-time inference.

| Model           | Silhouette Score | Calinski-Harabasz Score |
|------------------|------------------|-------------------------|
| **K-Means**      | **0.912553**     | **750248.478826**       |
| Hierarchical     | 0.898095         | 586158.031909           |
| GMM              | -0.442073        | 62.998815               |

- **Streamlit Application Development**:
  - Developed an interactive and user-friendly application using **Streamlit**.
  - Integrated the trained **K-Means model** to provide restaurant recommendations dynamically based on user inputs like cuisine or dish type.
  - Implemented interactive **visualizations** (e.g., maps with markers, charts for ratings and costs) using **Streamlit's plotting libraries**.
  - Designed the UI to display restaurant clusters with user-friendly filters and dynamic tables.

- **Chatbot Integration**:
  - Designed and integrated a chef-like chatbot assistant, **'Chef Mate: Assistant'**, using conversational AI APIs.
  - Limited chatbot functionality to focus exclusively on food recipe queries, ignoring unrelated topics.
  - Provided users with real-time cooking guidance by accessing recipe data from the preprocessed dataset stored in AWS RDS.

- **Deployment**:
  - Deployed the complete application (Streamlit app and trained model) on an **AWS EC2 instance** for real-time accessibility.
  - Configured the EC2 instance with necessary software (Python, Streamlit, and required libraries).
  - Set up security groups to enable secure HTTP access and limited permissions for interacting with AWS services.

- **Performance Optimization**:
  - Cached frequent database queries in the Streamlit application to improve response times.
  - Minimized latency by optimizing preprocessing scripts and reducing unnecessary computations.
  - Used AWS S3 and RDS for scalability and reliable data storage.

---

## ***Results***
- Restaurant recommendations based on clustering of user inputs.
- Interactive maps and visual metrics for better user insights.
- Real-time chatbot for assisting with recipe preparation.
- A fully functional and user-friendly web application.

---

## ***Project Evaluation Metrics***
- **Recommendation Accuracy**: Feedback-driven evaluation.
- **Chatbot Effectiveness**: Success rate of recipe query resolutions.
- **Application Responsiveness**: Speed of recommendations and chatbot responses.
- **User Engagement**: Interaction count and session duration.

---

## ***Dataset***
- **Source**: Zomato dataset in JSON format.
- **Variables**:
  - Restaurant ID, Name, Location, Cuisine, Ratings
  - Average Cost for Two, Price Range
  - Features (Table Booking, Online Delivery)
  - Longitude, Latitude
- **Preprocessing**:
  - Handle missing/inconsistent values.
  - Convert JSON to structured SQL tables.
  - Extract relevant features for recommendations.

---

## ***Technical Tags***
`Streamlit` `AWS S3` `AWS RDS` `AWS EC2` `Machine Learning` `Clustering` `Chatbot` `Data Visualization` `Python`
