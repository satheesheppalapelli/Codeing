{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "PythonPractise.py",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/satheesheppalapelli/Codeing/blob/master/PythonPractise.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "MAF8iO1iKBTk",
        "colab_type": "code",
        "outputId": "7506bc2c-3251-4fe2-bc74-e1f0197dff9c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print('Hello World')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello World\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "yqulzjNhLGdf",
        "colab_type": "code",
        "outputId": "92c64ef3-3d9f-41fb-c31f-42da72b13ab6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 153
        }
      },
      "cell_type": "code",
      "source": [
        "# Simple arithmetic\n",
        "\n",
        "# Addition\n",
        "print(2 + 3) \n",
        "\n",
        "# Subtraction\n",
        "print(5 - 2)\n",
        "\n",
        "# Multiplication\n",
        "print(6 * 5) \n",
        "\n",
        "# Division\n",
        "print(1 / 2) \n",
        "\n",
        "# classic division returns a float\n",
        "print(17 / 3)  \n",
        "\n",
        "# floor division\n",
        "print(17 // 3)  \n",
        "# \"//\" for integer part \n",
        "\n",
        "# double(**) power\n",
        "# 2 Power 3 (2*2*2) = 8  \n",
        "print(2 ** 3) \n",
        "\n",
        "# single(*) for number of times \n",
        "\n",
        "print(2 * 3)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5\n",
            "3\n",
            "30\n",
            "0.5\n",
            "5.666666666666667\n",
            "5\n",
            "8\n",
            "6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "Qj0tQC9q21zg",
        "colab_type": "code",
        "outputId": "65262367-6b0a-47ad-b6b7-06c5ad348887",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "cell_type": "code",
      "source": [
        "# Loops : Loops are a way to repeatedly execute some code statement\n",
        "\n",
        "planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']\n",
        "for planet in planets:\n",
        "    print(planet, end=' ')\n",
        "    \n",
        "multiplicands = (2, 2, 2, 3, 3, 5)\n",
        "product = 1\n",
        "for mult in multiplicands:\n",
        "    product = product * mult\n",
        "print(\"\\n\"+ str(product))\n",
        "\n",
        "\n",
        "\n",
        "# Notice the simplicity of the for loop: we specify the variable we want to use, \n",
        "# the sequence we want to loop over, and use the \"in\" keyword to link them together in an intuitive and readable way.\n",
        "\n",
        "# The object to the right of the \"in\" can be any object that supports iteration. \n",
        "# Basically, if it can be thought of as a sequence or collection of things, \n",
        "# you can probably loop over it. In addition to lists, we can iterate over the elements of a tuple:\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune \n",
            "360\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "ThG_9w6i_zPl",
        "colab_type": "code",
        "outputId": "41d68109-22cb-4853-c40b-a09bfa4d1060",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# And even iterate over each character in a string:\n",
        "s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'\n",
        "msg = ''\n",
        "# print all the uppercase letters in s, one at a time\n",
        "for char in s:\n",
        "    if char.isupper():\n",
        "        print(char, end='') "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "HELLO"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "-6S68lSxDTr8",
        "colab_type": "code",
        "outputId": "b66efbec-8a7b-4048-8ed0-bcf64b0debb9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        }
      },
      "cell_type": "code",
      "source": [
        "#  range() is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.\n",
        "\n",
        "# For example, if we want to repeat some action 5 times:\n",
        "\n",
        "for i in range(5):\n",
        "    print(\"Doing important work =\" , i)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Doing important work = 0\n",
            "Doing important work = 1\n",
            "Doing important work = 2\n",
            "Doing important work = 3\n",
            "Doing important work = 4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "GIJszDvmECPw",
        "colab_type": "code",
        "outputId": "28ce9f8a-1a91-4a70-e7d5-697d17c49777",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "cell_type": "code",
      "source": [
        "# You might assume that range(5) returns the list [0, 1, 2, 3, 4]. The truth is a little bit more complicated:\n",
        "# range(start,end,step)\n",
        "\n",
        "r = range(0,5,2)\n",
        "# r = range(5)\n",
        "print(r)\n",
        "\n",
        "# help(range)\n",
        "\n",
        "for i in range(0,5,2):\n",
        "    print(\"Doing important work. i =\" , i)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "range(0, 5, 2)\n",
            "Doing important work. i = 0\n",
            "Doing important work. i = 2\n",
            "Doing important work. i = 4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "KOd5XqeJHTGh",
        "colab_type": "code",
        "outputId": "2813faae-c8a8-4da5-9832-6dd4d7241bf3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "cell_type": "code",
      "source": [
        "# Just as we can use int(), float(), and bool() to convert objects to another type,\n",
        "# we can use list() to convert a list-like thing into a list, which shows a more familiar (and useful) representation:\n",
        "\n",
        "# range(5) produces 0, 1, 2, 3, 4. These are exactly the valid indices for a list of 4 elements.\n",
        "\n",
        "print(range(5))\n",
        "#  0, 1, 2, 3, 4\n",
        "print(list(range(5)))\n",
        "# [0, 1, 2, 3, 4]\n",
        "\n",
        "\n",
        "nums = [1, 2, 4, 8, 16]\n",
        "# So for any list L, for i in range(len(L)): will iterate over all its valid indices.\n",
        "for i in range(len(nums)):\n",
        "    nums[i] = nums[i] * 2\n",
        "print(nums)\n",
        "\n",
        "# This is the classic way of iterating over the indices of a list or other sequence.\n",
        "\n",
        "# Aside: for i in range(len(L)): is analogous to constructs like for (int i = 0; i < nums.length; i++) in other languages."
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "range(0, 5)\n",
            "[0, 1, 2, 3, 4]\n",
            "[2, 4, 8, 16, 32]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "xLRXSdnM2nlP",
        "colab_type": "code",
        "outputId": "e62e7ff9-ce6a-4755-c195-484b88a7d478",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "cell_type": "code",
      "source": [
        "# Dict_Compreshion {key:value} \n",
        "\n",
        "nums = [1,2,3,4,5,6,7,8]\n",
        "dict_comprehesion = {str(n): {\"The corresponding key is: \" + str(n)} for n in nums}\n",
        "print(dict_comprehesion)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'1': {'The corresponding key is: 1'}, '2': {'The corresponding key is: 2'}, '3': {'The corresponding key is: 3'}, '4': {'The corresponding key is: 4'}, '5': {'The corresponding key is: 5'}, '6': {'The corresponding key is: 6'}, '7': {'The corresponding key is: 7'}, '8': {'The corresponding key is: 8'}}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "J11zbs5P2yHb",
        "colab_type": "code",
        "outputId": "a06f8834-d966-4daa-ac77-0c291f9f9613",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# list_Compreshion\n",
        "nums = 'human beings'\n",
        "list_comprehesion = [n for n in nums]\n",
        "print(list_comprehesion)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['h', 'u', 'm', 'a', 'n', ' ', 'b', 'e', 'i', 'n', 'g', 's']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "gXw3zFbDJHaN",
        "colab_type": "code",
        "outputId": "6f0ade20-5cca-4a2b-e9a2-300f9f54d5b8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# enumerate function\n",
        "# for foo in x loops over the elements of a list and for i in range(len(x)) loops over the indices of a list. \n",
        "# What if you want to do both?\n",
        "\n",
        "# Enter the enumerate function, one of Python's hidden gems:\n",
        "\n",
        "def double_odds(nums):\n",
        "    for i, num in enumerate(nums):\n",
        "        if num % 2 == 1:\n",
        "            nums[i] = num * 2\n",
        "\n",
        "x = list(range(10))\n",
        "double_odds(x)\n",
        "print(x)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 2, 2, 6, 4, 10, 6, 14, 8, 18]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "Z3SVJO_MqEgu",
        "colab_type": "code",
        "outputId": "d6d6a02e-a720-4ec9-8364-626551bbe888",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "cell_type": "code",
      "source": [
        "### Electricity === Domestic or Commerical \n",
        "\n",
        "cat = input(\"Enter domestic or commerical:\")\n",
        "unit = int(input(\"Enter units:\"))\n",
        "if cat == 'domestic':\n",
        "    if unit < 100:\n",
        "        print(unit * 1)\n",
        "    elif unit >= 100 and unit < 200:\n",
        "        print(unit * 2)\n",
        "    elif unit >= 200:\n",
        "        print(unit * 3)\n",
        "    else:\n",
        "        print(\"Units Exceeded\")\n",
        "elif cat == 'commerical':\n",
        "    if unit < 100:\n",
        "        print(unit * 2)\n",
        "    elif unit >= 100 and unit < 200:\n",
        "        print(unit * 3)\n",
        "    elif unit >= 200:\n",
        "        print(unit * 4)\n",
        "    else:\n",
        "        print(\"Units Exceeded\")\n",
        "else:    \n",
        "    print(\"Enter valid input\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter domestic or commerical:domestic\n",
            "Enter units:40\n",
            "40\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "649VkYZzjG0-",
        "colab_type": "code",
        "outputId": "f4623e84-818f-414f-e8fe-4f6d5f5a16d6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "cell_type": "code",
      "source": [
        "import math \n",
        "\n",
        "def area():\n",
        "    radii = [1.2,1.3,1.4,1.5,2.1,2.3,2.4]\n",
        "    areas = []\n",
        "    for r in radii:\n",
        "        a = math.pi * (r ** 2)\n",
        "        areas.append(a)\n",
        "    return areas\n",
        "\n",
        "area()\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[4.523893421169302,\n",
              " 5.3092915845667505,\n",
              " 6.157521601035993,\n",
              " 7.0685834705770345,\n",
              " 13.854423602330987,\n",
              " 16.619025137490002,\n",
              " 18.09557368467721]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "metadata": {
        "id": "YDrGIgzu6GL8",
        "colab_type": "code",
        "outputId": "9aa15fd2-3049-4a41-9de2-4325b57fcf9f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# function calling another function\n",
        "def f(n):\n",
        "    return g(n+1)\n",
        "\n",
        "def g(y):\n",
        "    return y+3\n",
        "\n",
        "z = f(4)\n",
        "print(z)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "kcs1dK8d5eoP",
        "colab_type": "code",
        "outputId": "bff45480-d10c-4dfb-bb85-4ae9d61a416a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# fuction calling itself is a Recursion\n",
        "# Recursion of a Factorial\n",
        "def fact(n):\n",
        "    if n == 0 :\n",
        "        return 1\n",
        "    else:\n",
        "        value = n * fact(n-1)\n",
        "        return value\n",
        "fact(5)\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "120"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "metadata": {
        "id": "taQjLr5TjMSf",
        "colab_type": "code",
        "outputId": "b86ae038-64c3-4aec-c07b-e28814b95fdc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "# fuction calling itself is a Recursion\n",
        "# Recursion of a Multilication\n",
        "def multiply(m,n):\n",
        "    if n == 1:\n",
        "        return m\n",
        "    else:\n",
        "        return m + multiply(m,n-1)\n",
        "\n",
        "multiply(2,3)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "metadata": {
        "id": "pTIaDDWvjk0d",
        "colab_type": "code",
        "outputId": "37a37637-b4ec-4624-f386-bf7b35465d4e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 435
        }
      },
      "cell_type": "code",
      "source": [
        "def length(*l):\n",
        "    if l == []:\n",
        "        return 0\n",
        "    else:\n",
        "        return 1 + length(l[1:])\n",
        "length(1,2,3,4,5)          "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "RecursionError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-31-c41bef4d4a1a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-31-c41bef4d4a1a>\u001b[0m in \u001b[0;36mlength\u001b[0;34m(*l)\u001b[0m\n\u001b[1;32m      3\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "... last 1 frames repeated, from the frame below ...\n",
            "\u001b[0;32m<ipython-input-31-c41bef4d4a1a>\u001b[0m in \u001b[0;36mlength\u001b[0;34m(*l)\u001b[0m\n\u001b[1;32m      3\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mRecursionError\u001b[0m: maximum recursion depth exceeded in comparison"
          ]
        }
      ]
    },
    {
      "metadata": {
        "id": "pUmPoXcykHLW",
        "colab_type": "code",
        "outputId": "f22430d7-4f40-458a-ea72-54337a0be09a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        }
      },
      "cell_type": "code",
      "source": [
        "def sumlist(l):\n",
        "    if l == []:\n",
        "        return(0)\n",
        "    else:\n",
        "        return(l[0] + sumlist(l[1:])\n",
        "sumlist(1)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-387b3e4cffb2>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    sumlist(1)\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "id": "K9JVFeRb8EGX",
        "colab_type": "code",
        "outputId": "489349f2-a3a9-4e70-e9d7-917b61886a6d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "#  factor of a number\n",
        "def factors(n):\n",
        "    factorlist = []\n",
        "    for i in range(1,n+1):\n",
        "        if n%i == 0:\n",
        "            factorlist = factorlist + [i]\n",
        "    return factorlist\n",
        "\n",
        "def isprime(n):\n",
        "    return(factors(n) == [1,n])\n",
        "\n",
        "def primesupto(n):\n",
        "    primelist = []\n",
        "    for i in range(1,n+1):\n",
        "        if isprime(i):\n",
        "            primelist = primelist + [i]\n",
        "    return(primelist)\n",
        "\n",
        "def nprimes(n):\n",
        "    (count,i,plist) = (0,1,[])\n",
        "    while(count < n):\n",
        "        if isprime(i):\n",
        "            (count,plist) = (count+1,plist+[i])\n",
        "        i = i+1\n",
        "    return(plist)\n",
        "\n",
        "factors(5)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 5]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "metadata": {
        "id": "vo1lPaj5DV34",
        "colab_type": "code",
        "outputId": "665bbc34-cc4b-46f5-d4b4-b3a78bc26d20",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 231
        }
      },
      "cell_type": "code",
      "source": [
        "x = [1,\"abcd\",2,\"efgh\",[3,4]]  # Statement 1\n",
        "y = x[0:50]                    # Statement 2\n",
        "z = y                          # Statement 3\n",
        "w = x                          # Statement 4\n",
        "x[1] = x[1] + 'd'              # Statement 5\n",
        "x[1][1] = 'y'                # Statement 6\n",
        "y[2] = 4                       # Statement 7\n",
        "z[0] = 0                       # Statement 8\n",
        "w[4][0] = 1000                 # Statement 9\n",
        "a = (x[4][1] == 4) "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-16-0265fe1649ea>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mw\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mx\u001b[0m                          \u001b[0;31m# Statement 4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m'd'\u001b[0m              \u001b[0;31m# Statement 5\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'y'\u001b[0m                \u001b[0;31m# Statement 6\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m4\u001b[0m                       \u001b[0;31m# Statement 7\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mz\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m                       \u001b[0;31m# Statement 8\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
          ]
        }
      ]
    },
    {
      "metadata": {
        "id": "dZv1FX3NEwZE",
        "colab_type": "code",
        "outputId": "ddbfe216-79ee-4587-bb5c-32045215677b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        }
      },
      "cell_type": "code",
      "source": [
        "startmsg = \"hello\"\n",
        "endmsg = \"\"\n",
        "for i in range(0,len(startmsg)):\n",
        "    endmsg = startmsg[i] + endmsg\n",
        "    print(endmsg)\n",
        "print(endmsg)    "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "h\n",
            "eh\n",
            "leh\n",
            "lleh\n",
            "olleh\n",
            "olleh\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "1uKCNpq-FZ3e",
        "colab_type": "code",
        "outputId": "85f61b8f-8251-4303-8405-53b188b74d19",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def mystery(l):\n",
        "    l = l + l\n",
        "    return()\n",
        "\n",
        "mylist = [31,24,75]\n",
        "mystery(mylist)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "()"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 65
        }
      ]
    },
    {
      "metadata": {
        "id": "Spb8UnBgFrNN",
        "colab_type": "code",
        "outputId": "ab727327-1a68-4418-b306-0cb48f9d40f0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "cell_type": "code",
      "source": [
        "x = [13,4,17,1000]\n",
        "w = x[1:]\n",
        "u = x[1:]\n",
        "y = x\n",
        "u[0] = 50\n",
        "print(u)\n",
        "y[1] = 40\n",
        "print(y)\n",
        "print(w)\n",
        "print(x[1], y[1], w[0], u[0])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[50, 17, 1000]\n",
            "[13, 40, 17, 1000]\n",
            "[4, 17, 1000]\n",
            "40 40 4 50\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "aGYcPurwlP95",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "# Search for value in a list\n",
        "def findpos(list1, value):\n",
        "    # Return first position of v in l\n",
        "    # Return -1 if v not in l\n",
        "    (found, i) = (False, 0)\n",
        "    #   for i in range(len(l)):\n",
        "    #       if l[i] == v: # Exit, report position\n",
        "    #           pos = i\n",
        "    #           break\n",
        "    #   else:\n",
        "    #       pos = -1 # No break, v not in l\n",
        "\n",
        "    while i < len(list1):\n",
        "        if list1[i] == value:\n",
        "            (found, pos) = (True, i)\n",
        "    if not found:\n",
        "        pos = -1\n",
        "    return (pos)\n",
        "\n",
        "\n",
        "findpos(list1, value)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "8e6q5R4_acaI",
        "colab_type": "code",
        "outputId": "ee1b89e5-47c2-4186-9e8c-dcb14fc92b1a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "cell_type": "code",
      "source": [
        "class Fruit:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "\n",
        "    def love(self):\n",
        "        pass  # pass means do nothing\n",
        "\n",
        "\n",
        "class Mango(Fruit):\n",
        "    def love(self):\n",
        "        print(\"Lakshmi loves mangoes\")\n",
        "\n",
        "\n",
        "class Apple(Fruit):\n",
        "    def love(self):\n",
        "        print(\"Narine loves apples\")\n",
        "\n",
        "\n",
        "slice = Mango(\"Alphonso\")\n",
        "slice.name\n",
        "slice.love()\n",
        "appy = Apple(\"Kashmiri\")\n",
        "appy.name\n",
        "appy.love()\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Lakshmi loves mangoes\n",
            "Narine loves apples\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "ZfnRBTWaYO_7",
        "colab_type": "code",
        "outputId": "cfe28d46-0f61-4b8a-b5cc-8e6af0c99e0d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "class Point:\n",
        "  \n",
        "    def __init__(self, x = 0, y = 0):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "  \n",
        "    def __sub__(self, other):\n",
        "        x = self.x + other.x\n",
        "        y = self.y + other.y\n",
        "        return Point(x,y)\n",
        "        \n",
        "p1 = Point(3, 4)\n",
        "p2 = Point(1, 2)\n",
        "result = p1-p2\n",
        "print(result.x, result.y)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "4 6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "vnE8_3cLAwlk",
        "colab_type": "code",
        "outputId": "ffd3810a-2d4f-48d1-bf2e-c229969c83b1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def transpose(m):\n",
        "    # iterate through rows\n",
        "    for i in range(len(m[0])):\n",
        "   # iterate through columns\n",
        "        for j in range(len(m[0])):\n",
        "            m[i][j] = m[j][i]\n",
        "    for r in m:\n",
        "        return r\n",
        "        \n",
        "        \n",
        "transpose([[1,1,1],[2,2,2],[3,3,3]])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "metadata": {
        "id": "tZmgxhffW78F",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "What is **Decoraters** and How to use it ?\n",
        "\n",
        "**A decorator takes in a function, adds some functionality and returns it. **\n",
        "A function takes an argument as a function and then return it. "
      ]
    },
    {
      "metadata": {
        "id": "9JNn2QjeXBgO",
        "colab_type": "code",
        "outputId": "f211baac-57a9-42af-debe-437fb3397693",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "cell_type": "code",
      "source": [
        "def smart_divide(func):\n",
        "    def inner(a,b):\n",
        "        print(\"I am going to divide\",a,\"and\",b)\n",
        "        if b == 0:\n",
        "            print(\"Whoops! cannot divide\")\n",
        "            return\n",
        "        return func(a,b)\n",
        "    return inner\n",
        "\n",
        "@smart_divide\n",
        "def divide(a,b):\n",
        "    return a/b\n",
        "\n",
        "divide(4,2)\n",
        "divide(2,0)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "I am going to divide 4 and 2\n",
            "I am going to divide 2 and 0\n",
            "Whoops! cannot divide\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "KCPL6PAtcskP",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "**What is Generator?**\n",
        "\n",
        "If a function contains at least one **yield** statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.\n",
        "\n",
        "The difference is that, while a **return** statement terminates a function entirely, **yield** statement pauses the function saving all its states and later continues from there on successive calls."
      ]
    },
    {
      "metadata": {
        "id": "Nos7InBkiMqe",
        "colab_type": "code",
        "outputId": "1631192b-aeaa-4577-f29c-acfcfc94c105",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        }
      },
      "cell_type": "code",
      "source": [
        "# Initialize the list\n",
        "my_list = [1, 3, 6, 10]\n",
        "\n",
        "# # square each term using list comprehension\n",
        "# # Output: [1, 9, 36, 100]\n",
        "# [x**2 for x in my_list]\n",
        "\n",
        "# # same thing can be done using generator expression\n",
        "# # Output: <generator object <genexpr> at 0x0000000002EBDAF8>\n",
        "# (x**2 for x in my_list)\n",
        "\n",
        "a = (x**2 for x in my_list)\n",
        "print(type(a))\n",
        "# Output: 1\n",
        "print(next(a))\n",
        "\n",
        "# Output: 9\n",
        "print(next(a))\n",
        "\n",
        "# Output: 36\n",
        "print(next(a))\n",
        "\n",
        "# Output: 100\n",
        "print(next(a))\n",
        "\n",
        "# Output: StopIteration\n",
        "next(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'generator'>\n",
            "1\n",
            "9\n",
            "36\n",
            "100\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "StopIteration",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-23-a33b1f1adf45>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# Output: StopIteration\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mStopIteration\u001b[0m: "
          ]
        }
      ]
    },
    {
      "metadata": {
        "id": "Oo1sKEPOctNV",
        "colab_type": "code",
        "outputId": "fc6d8b62-b36e-41c7-a753-2e241efa088c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        }
      },
      "cell_type": "code",
      "source": [
        "# A simple generator function\n",
        "def my_gen():\n",
        "    n = 1\n",
        "    print('This is printed first')\n",
        "    # Generator function contains yield statements\n",
        "    yield n\n",
        "    n += 1\n",
        "    print('This is printed second')\n",
        "    yield n\n",
        "\n",
        "    n += 1\n",
        "    print('This is printed at last')\n",
        "    yield n\n",
        "\n",
        "for item in my_gen():\n",
        "    print(item)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "This is printed first\n",
            "1\n",
            "This is printed second\n",
            "2\n",
            "This is printed at last\n",
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "LufTYdqTg-k1",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "A **generator** that reverses a string."
      ]
    },
    {
      "metadata": {
        "id": "u2ZRnR5QgNMD",
        "colab_type": "code",
        "outputId": "223796a5-330d-40c4-972e-f8539da2d5c8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def rev_str(my_str):\n",
        "    length = len(my_str)\n",
        "    for i in range(length - 1,-1,-1):\n",
        "        yield my_str[i]\n",
        "\n",
        "# For loop to reverse the string\n",
        "# Output: hseehtaS\n",
        "name = ' '\n",
        "for char in rev_str(\"Satheesh\"):\n",
        "    name = name + str(char)\n",
        "print(name)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " hseehtaS\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "zd6XXa8nq17a",
        "colab_type": "code",
        "outputId": "a00cd4e3-a3d5-4156-b347-c041067ccdbb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "cell_type": "code",
      "source": [
        "# our two sum function which will return\n",
        "# all pairs in the list that sum up to target_sum\n",
        "def twosum(numbers,target_sum):\n",
        "    sums = []\n",
        "    # check each element in array\n",
        "    for i in range(0,len(numbers)):\n",
        "        # check each other element in the array\n",
        "        for j in range(i+1, len(numbers)):\n",
        "            # determine if these two elements sum to target_sum\n",
        "            if numbers[i] + numbers[j] == target_sum:\n",
        "                sums.append([numbers[i], numbers[j]])\n",
        "                print(numbers[i], '+', numbers[j], '=', target_sum)\n",
        "                # return all pairs of integers that sum to target_sum\n",
        "    return sums\n",
        "\n",
        "\n",
        "print(twosum([3,2,4,6,7,8],10))\n",
        "print(twosum([3, 5, 2, -4, 8, 11], 7))                 \n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3 + 7 = 10\n",
            "2 + 8 = 10\n",
            "4 + 6 = 10\n",
            "[[3, 7], [2, 8], [4, 6]]\n",
            "5 + 2 = 7\n",
            "-4 + 11 = 7\n",
            "[[5, 2], [-4, 11]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "zdasKrWyPzt_",
        "colab_type": "code",
        "outputId": "beb0421a-acc4-4e9b-f296-1ad9ebd07c0f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "cell_type": "code",
      "source": [
        "def print_rangoli(size):\n",
        "    # your code goes here\n",
        "    for i in range(0, size):\n",
        "        for j in range(0, size - i):\n",
        "            print('-', end=' ')\n",
        "        for k in range(0, i + 1):\n",
        "            print(' * ', end=' ')\n",
        "        for l in range(0, size - i):\n",
        "            print('-', end=' ')\n",
        "        print('\\r')\n",
        "        \n",
        "        \n",
        "    for m in range(0, size):\n",
        "        for n in range(0, m + 1):\n",
        "            print('-', end=' ')\n",
        "        for o in range(0, 6 - m):\n",
        "            print(' * ', end=' ')\n",
        "        for p in range(0, m + 1):\n",
        "            print('-', end=' ')\n",
        "        print('\\r')\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    n = int(input())\n",
        "    print_rangoli(n)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "6\n",
            "- - - - - -  *  - - - - - - \n",
            "- - - - -  *   *  - - - - - \n",
            "- - - -  *   *   *  - - - - \n",
            "- - -  *   *   *   *  - - - \n",
            "- -  *   *   *   *   *  - - \n",
            "-  *   *   *   *   *   *  - \n",
            "-  *   *   *   *   *   *  - \n",
            "- -  *   *   *   *   *  - - \n",
            "- - -  *   *   *   *  - - - \n",
            "- - - -  *   *   *  - - - - \n",
            "- - - - -  *   *  - - - - - \n",
            "- - - - - -  *  - - - - - - \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "Fam8ZfXLGjVH",
        "colab_type": "code",
        "outputId": "b83a33fc-fbf5-4f2e-c1d3-e96ca036e6db",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "class employee:\n",
        "    def __init__(self, firstname, lastname):\n",
        "        self.firstname= firstname\n",
        "        self.lastname= lastname\n",
        "    def describe(self):\n",
        "        print(\"firstname={}, lastname={}\".format(self.firstname, self.lastname))\n",
        "\n",
        "# if __name__ == \" __main__\":\n",
        "emp = employee('Satheesh','eppalapelli')\n",
        "emp.describe()\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "firstname=Satheesh, lastname=eppalapelli\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "eEi0O8p4PNyC",
        "colab_type": "code",
        "outputId": "be8dc570-ed0d-4f4d-feba-0856e00eb1fc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 293
        }
      },
      "cell_type": "code",
      "source": [
        "def pyramid(rows):\n",
        "    for i in range(rows):\n",
        "        spaces = rows - (i + 1)\n",
        "#         print(spaces)\n",
        "        stars = 2 * (i + 1) - 1\n",
        "#         print(stars)\n",
        "        output_row = spaces * \" \" + stars * \"*\"\n",
        "        print(output_row)\n",
        "pyramid(5)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "4\n",
            "1\n",
            "    *\n",
            "3\n",
            "3\n",
            "   ***\n",
            "2\n",
            "5\n",
            "  *****\n",
            "1\n",
            "7\n",
            " *******\n",
            "0\n",
            "9\n",
            "*********\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}