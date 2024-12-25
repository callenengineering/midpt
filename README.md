# Midpt (API)

## Description

Have you ever and your friends ever wanted to meet in the middle but it you had no idea where that was? This is the issue that Midpt wants to solve.

## Table of Contents

- [General Info](#general-info)
- [Installation](#installation)
- [FAQs](#faqs)

## General Info

Hosted [here]()

The POST endpoint takes in 3 parameters:

1. destination_type - string
2. max_radius (in meters) - integer
3. addresses\* - dictionary

### Example

---

Let's say you want to find the midpoint between the White House and the empire state building. Not only, that you want to find a coffee shop near the midpoint. We could make a request that looks something like this:

**Input**

![places_input_example](https://user-images.githubusercontent.com/70670609/214965961-9cfc8720-6fb3-414d-aac8-b126044d48cd.png)

**Output**

![places_output_example](https://user-images.githubusercontent.com/70670609/214965808-ca34d921-21fd-4a8e-b81c-23c24e0bda1a.png)

A full list of destination types can be found [here](https://developers.google.com/maps/documentation/places/web-service/supported_types)

## Installation

Midpt leverages Docker in order to handle building the application. You will need to have it installed before running this code. Docker installation instructions can be found [here](https://docs.docker.com/get-docker/).

Once you have Docker installed, follow the steps below:

- Clone the repo
- Run **make dev-rebuild** in your terminal

That's it! Visit http://localhost:8000/docs and start making requests.

## FAQs

**Can I find the midpoint for 3+ locations?**
Yes, you can! Enter all your addresses in the addresses array and Midpt will know what to do.

**What can I enter for destination type?**
A full list of allowed places can be found [here](https://developers.google.com/maps/documentation/places/web-service/supported_types)

**Why do I have longer drive than my friend?**
There are two reasons for this:

1. If you gave a destination type and a radius, the places may not be _exactly_ in the middle but it will be close
2. One route may be more direct than the other. If you have to take a side streets the whole way but your friend can fly on the highway, they will have a longer journey.
