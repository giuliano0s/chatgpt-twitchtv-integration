# chatgpt-twitchtv-integration

Simple integration between ChatGPT and the livestreaming platform Twitch TV.

# How to Use

## Browser Setup
- Download Google Chrome, create a user profile, and save the profile ID found under "Profile Path" in `chrome://version/`.
  - Example: `C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile 4` → the ID is `Profile 4`
- Go to [https://www.twitch.tv](https://www.twitch.tv), create a dedicated account for the bot and another one for yourself (if you don’t have one already). Preferably verify the email and password for both accounts.

## Code Configuration
- Insert the profile ID (e.g., `Profile 4`) in `pipeline.ipynb` > class `Utils` (second cell) > variable `profile_name`
- Set the parameters in the `Chatbot` class:
  - `botIdName` = Twitch username of the bot
  - `botName` = name to be interpreted by the bot
  - `fileName` = text file containing the prompt engineering
  - `streamId` = Twitch channel ID
  - `pronouns` = feminino/masculino (female/male respectively)
  - `mainUser` = your Twitch username
  - `openai_key` = your OpenAI API key

## Prompt Engineering
- There are 3 prompt examples available in `./Utils/characters`:
  - `butler.txt` = butler-style personality
  - `helto_hater.txt` = imitates someone who dislikes the streamer Helto
  - `musk.txt` = simulates Elon Musk’s persona

## Chatting with the Bot
- Go to the chat of the user specified in `streamId`
- Interact with the bot using `@{botIdName}` to address it
  - Example:
    - Input: `Hi @testingbot9966`
    - Output: `Hello! I’m Elon Musk! How can I help you?`

- Demo video: [YouTube](https://www.youtube.com/watch?v=xRfKNiUCWTg)
