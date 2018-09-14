# Cris overview

In this tutorial, we will charge the custom speech to text service, cris.ai, with one of the hardest task available : understanding the rpaper emimem, in the song "rap god".
The motivation (beyond "because I can") is to showcase the limits of the service, and therefore it application domain.


## Prerequisites

To create a custom Speech-to-text model, you need three things : an audio dataset, a text dataset, and a cris.ai account. You then can create an accoustic model linking the audio to the text within cris.ai.

### The audio dataset

It has a few format requirements : you need a .wav format, in mono, with a debit of 16KB/s. Each sentence requires to be in its own file. It's the most boring part in the job.

### The text dataset

It is a .txt with the following architecture : 

### The cris.ai model

When you have both audio and text, you can create an acoustic model which will adapt to the context. Depending on your needs, you might need to get a subscription in the Azure portal -however everything I did for testing was free.


## The training


## The precision

open a tunnel 
```bash
ssh -D 127.0.0.1:8034 $pyp17vmname.westeurope.cloudapp.azure.com
```

then have your browser using the ssh tunnel as a proxy. Here is how this looks in Firefox (which as proxy settings independant of the OS):
![](img/firefoxproxy.png)

