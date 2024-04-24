---
layout: home
title: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services
permalink: /
---

**TL;DR:** Large language models (LLMs) have revolutionized text-based interactions, enabling services from real-time translation to AI-driven chatbots by streaming tokens to users, akin to video streaming. Such text streaming service allows users to digest the content incrementally, whether in text or speech form. However, existing serving systems primarily focus on optimizing server-side aggregated metrics like token generation throughput, ignoring individual user experience with streamed text. As a result, under high and/or bursty load, a significant number of users can receive unfavorable service quality or poor Quality-of-Experience (QoE).

In this project, we first formally define QoE of text streaming services by considering the end-to-end token delivery process throughout the entire interaction with the user. Thereafter, we propose Andes, a QoE-aware serving system that enhances user experience for LLM-enabled text streaming services. At its core, Andes strategically allocates contended GPU resources among multiple requests over time to optimize their QoE. Our evaluations demonstrate that, compared to the state-of-the-art LLM serving systems like vLLM, Andes improves the average QoE by up to 3.2× under high request rate, or alternatively, it attains up to 1.6× higher request rate while preserving high QoE.


## A User-Side Story