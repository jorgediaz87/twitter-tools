# Twitter Tools
This is a personal project to learn how to use technologies like Vue or Flask.

Twitter management tools to block bots and hoaxes accounts easily and perform batch actions.

## Update

I will not maintain this repository anymore because I deleted my Twitter account. It is no longer an interesting social network for me, it only promotes hatred, confrontation and lies. 
If you want to keep the project feel free to fork it out and if you have any doubt, don't hesitate to ask me.

There are some functions that are still unfinished and some that I have not been able to implement, but for the most part they should fulfill their objective.

## Requirements

- Twitter developer account
- Python3
- Node.js
- npm

## Installation

Clone the proyect from the repository:

```bash
git clone https://github.com/zepo87/twitter-tools.git
```

Install python requirements:

```bash
pip install -r requirements.txt
```

Populate .env in the *app* folder file with your own credentials:
```
API_KEY=
API_SECRET=
TOKEN=
TOKEN_SECRET=
```

Install the frontend (in app/frontend):

```bash
npm install
```

Run serve the frontend in your local enviroment:


```bash
npm run serve
```
**Please note that you are likely to have problems with CORS**
To avoid them I did my test running chrome with the following command.
```
google-chrome --disable-web-security -–allow-file-access-from-files
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
