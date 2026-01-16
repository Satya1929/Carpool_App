<div align="left" style="position: relative;">
<h1>CARPOOL_APP</h1>
<p align="left">
	<em><code>Streamlit-based carpool dashboard using Google Sheets</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/Satya1929/Carpool_App?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Satya1929/Carpool_App?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Satya1929/Carpool_App?style=default&color=0080ff" alt="repo-top-language">
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [⚙️ How It Works](#-how-it-works)
- [🖼️ Preview](#-preview)
- [👾 Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗️ License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview
**V_Carpool** is a community-driven carpooling application built with **Python** and **Streamlit**. It acts as a matchmaking platform for travelers—primarily university students and daily commuters—helping them find compatible partners based on shared preferences and travel dates.

By leveraging **Google Sheets** as a real-time backend, V_Carpool collects user submissions via Google Forms and dynamically displays them in a clean, searchable dashboard.

---

## ⚙️ How It Works
1. **Submit**: Users enter travel details (date, time, destination) via a **Google Form**.
2. **Sync**: The data is instantly stored in a **Google Sheet**.
3. **Match**: This **Streamlit** app fetches the sheet data in real-time, allowing users to search and discover travel partners.

---

<!-- ## 🖼️ Preview
> [!TIP]
> Add a screenshot of your dashboard here to wow your users!
> `<img src="path/to/your/screenshot.png" alt="Carpool App Dashboard" width="100%">`

--- -->

## 👾 Features

- **🏠 Smart Preference Collection**: Users easily submit travel details (Date, Time, Destination, Notes) to a centralized database.
- **🔎 Search by Date**: Select a specific travel date to see a list of potential partners displayed in clean, informative user cards.
- **📊 Dynamic Data Visualization**: Interactive pie charts visualize the distribution of travel times and popular destinations for any selected date.
- **⚡ Real-Time Dashboard**: "All Days Summary" provides a bird's-eye view of travel trends across the entire dataset, always synced with the latest entries.
- **🎉 Credits**: Dedicated section acknowledging the developer and contributors.

---

## 🛠️ Tech Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Language:** [Python](https://www.python.org/)
- **Data Engineering:** [Pandas](https://pandas.pydata.org/)
- **Data Visualization:** [Matplotlib](https://matplotlib.org/)
- **Database/Storage:** [Google Sheets API](https://developers.google.com/sheets/api)

---

## 📁 Project Structure

```sh
└── Carpool_App/
    ├── main.py
    ├── utils.py
    ├── test_app.py
    ├── packages.txt
    ├── pages/
    │   ├── 1_🔎_Search_by_Date.py
    │   ├── 2_📊_All Days_Summary.py
    │   └── 3_🎉_Credits_Page.py
    └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>CARPOOL_APP/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/main.py'>main.py</a></b></td>
				<td>Entry point: Landing page and navigation logic</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/utils.py'>utils.py</a></b></td>
				<td>Core utility functions (NaN handling, time categorization)</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/test_app.py'>test_app.py</a></b></td>
				<td>Unit tests for verification of utility logic</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Python package dependencies</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/packages.txt'>packages.txt</a></b></td>
				<td>List of OS packages (currently empty)</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- pages Submodule -->
		<summary><b>pages</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/pages/3_🎉_Credits_Page.py'>3_🎉_Credits_Page.py</a></b></td>
				<td>Credits page</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/pages/1_🔎_Search_by_Date.py'>1_🔎_Search_by_Date.py</a></b></td>
				<td>Search results by date</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Satya1929/Carpool_App/blob/master/pages/2_📊_All Days_Summary.py'>2_📊_All Days_Summary.py</a></b></td>
				<td>Aggregated travel summary</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Carpool_App, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.8+
- **Package Manager:** Pip


### ⚙️ Installation

Install Carpool_App using one of the following methods:

**Build from source:**

1. Clone the Carpool_App repository:
```sh
❯ git clone https://github.com/Satya1929/Carpool_App
```

2. Navigate to the project directory:
```sh
❯ cd Carpool_App
```

3. Install the project dependencies:

```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage
Run Carpool_App using the following command:

```sh
❯ streamlit run main.py
```


### 🧪 Testing
The project includes a suite of unit tests to verify data processing utilities.

**Run the test suite using:**
```sh
❯ python -m pytest test_app.py
```


---
## 📌 Project Roadmap

- [X] **`Phase 1`**: Successfully deployed with 1000+ active users.
- [ ] **`Phase 2`**: Implement bidirectional filtering (Campus to Home / Home to Campus).
- [ ] **`Phase 3`**: Develop AI-powered matchmaking and user authentication.

---

## 🔰 Contributing

- ** [Report Issues](https://github.com/Satya1929/Carpool_App/issues)**: Submit bugs found or log feature requests for the `Carpool_App` project.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Satya1929/Carpool_App
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch.
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/Satya1929/Carpool_App/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Satya1929/Carpool_App">
   </a>
</p>
</details>

---

## 🎗️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🙌 Acknowledgments

- Built with [Streamlit](https://streamlit.io/).
- Data powered by [Google Sheets](https://www.google.com/sheets/about/).

---
