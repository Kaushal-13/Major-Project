{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": " Major Project.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kaushal-13/Major-Project/blob/main/App.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9JAN4mbYFdP-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3c979b45-5aee-456c-a3de-62a533a5f0c3"
      },
      "source": [
        "!pip install streamlit --quiet\n",
        "!pip install pyngrok==4.1.1\n",
        "from pyngrok import ngrok\n"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\u001b[K     |████████████████████████████████| 7.8MB 4.0MB/s \n",
            "\u001b[K     |████████████████████████████████| 112kB 44.0MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.2MB 42.2MB/s \n",
            "\u001b[K     |████████████████████████████████| 81kB 9.5MB/s \n",
            "\u001b[K     |████████████████████████████████| 174kB 32.5MB/s \n",
            "\u001b[K     |████████████████████████████████| 122kB 41.1MB/s \n",
            "\u001b[K     |████████████████████████████████| 71kB 8.3MB/s \n",
            "\u001b[?25h  Building wheel for blinker (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[31mERROR: google-colab 1.0.0 has requirement ipykernel~=4.10, but you'll have ipykernel 5.5.5 which is incompatible.\u001b[0m\n",
            "Collecting pyngrok==4.1.1\n",
            "  Downloading https://files.pythonhosted.org/packages/e4/a9/de2e15c92eb3aa4a2646ce3a7542317eb69ac47f667578ce8bf916320847/pyngrok-4.1.1.tar.gz\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.1) (0.16.0)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.1) (3.13)\n",
            "Building wheels for collected packages: pyngrok\n",
            "  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyngrok: filename=pyngrok-4.1.1-cp37-none-any.whl size=15985 sha256=a3e15a25ea7c6938a85ef6bef957f2c002aaedcd64c5a1dd0a4e62eafbc7f1ed\n",
            "  Stored in directory: /root/.cache/pip/wheels/97/71/0d/1695f7c8815c0beb3b5d9b35d6eec9243c87e6070fbe3977fa\n",
            "Successfully built pyngrok\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-4.1.1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FKJXXYOVHYrX",
        "outputId": "4fa568b7-d9b7-416a-de42-9f37ab48e64b"
      },
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st \n",
        "import os\n",
        "from textblob import TextBlob \n",
        "\n",
        "# Title\n",
        "st.title(\"Sentiment Analysis\")\n",
        "\n",
        "result_sentiment = 2\n",
        "# Sentiment Analysis\n",
        "st.subheader(\"Analyse Your Text\")\n",
        "\n",
        "message = st.text_area(\"Enter Text\")\n",
        "if st.button(\"Analyze\"):\n",
        "\t\t\tblob = TextBlob(message)\n",
        "\t\t\tresult_sentiment = blob.sentiment[0]\n",
        "\t\t\t\n",
        "    \n",
        "if result_sentiment > 0.5 and result_sentiment < 1 :\n",
        "      st.write('Prediction  :')\n",
        "      st.subheader('Positive')\n",
        "      st.success(f'Score : {result_sentiment}')\n",
        "\n",
        "elif result_sentiment < 0 :\n",
        "      st.write('Prediction  :')\n",
        "      st.subheader('Negative')\n",
        "      st.success(f'Score : {result_sentiment}')\n",
        "elif result_sentiment >= 0 and result_sentiment <= 0.5 :\n",
        "      st.write('Prediction  :')\n",
        "      st.subheader('Neutral')\n",
        "      st.success(f'Score : {result_sentiment}')\n"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Overwriting app.py\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "AsKwOrORHcmG",
        "outputId": "822ed858-80c4-4c90-87fa-cad4059f71b9"
      },
      "source": [
        "!nohup streamlit run app.py &\n",
        "\n",
        "url = ngrok.connect(port='8501')\n",
        "url\n",
        "#HERE WE GET A LINK WHICH IS TO BE COPIED"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "nohup: appending output to 'nohup.out'\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'http://533a10900ddb.ngrok.io'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hoDZ0XST7wrw"
      },
      "source": [
        ""
      ],
      "execution_count": 3,
      "outputs": []
    }
  ]
}