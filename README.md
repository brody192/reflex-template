<p align="center">
    <a href="https://reflex.dev/">
        <img style="border-radius: 5px" src="https://pbs.twimg.com/profile_banners/1580292598874271746/1690936236" alt="Logo" width="500">
    </a>
</p>

<p align="center">Web apps in pure Python, Built in a few minutes!</p>
<p align="center">Build anything, faster</p>

Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/A5TaaV?referralCode=ySCnWl)

## Any use case

With Reflex you can build anything from internal tools and data apps to complex multi-page apps

## It's just Python

The app state is just a class. State updates are methods in the class. And the UI is a reflection of the state

## Write your entire app in Python [Frontend]

**No more switching between languages and frameworks. Use one language for your whole stack**

- **60+ built-in UI Components**

    Reflex comes with a large library of UI components ranging from simple buttons to complex graphs and tables.

    [Check out the full library](https://reflex.dev/docs/library/)

- **Custom Components**

    Create your own components in a few lines of code. Simply wrap the React component of your choice.

    [Wrapping React Guide](https://reflex.dev/docs/advanced-guide/wrapping-react/)

- **Completely customizable**

    All Reflex components are fully customizable. Change the colors, fonts, and styles to match your project

    [Styling Guide](https://reflex.dev/docs/styling/overview/)

- **Now everyone can work across the full-stack**

    With Reflex every engineer can work across the whole stack allowing for a more efficient and productive workflow

## Skip the boilerplate and get started faster [Backend]

**Reflex comes with a powerful backend built with FastAPI and SQLAlchemy**

- **Batteries included**

    Skip the boilerplate and get started faster. Reflex integrates the frontend and backend so there is no need to write API endpoints

    [State docs](https://reflex.dev/docs/state/overview/)

- **Seamlessly integrate with any Python library**

    Never get locked into a framework that doesn't support your existing tech stack

- **Built in database ORM**

    Integrate with existing databases with a single line of code. Or use our built in SQLite database

    [Database docs](https://reflex.dev/docs/database/overview/)

## What makes this work on Railway?

- **Custom build plan:** [nixpacks.toml](https://github.com/brody192/reflex-template/blob/main/nixpacks.toml)

    - Runs all the necessary commands to setup, initialize, export, and install Caddy
    - Starts the Reflex backend and Caddy server using [parallel](https://www.gnu.org/software/parallel/) to avoid having to run two separate services in the project

- **The [Caddy](https://caddyserver.com/) Server/Proxy:** [Caddyfile](https://github.com/brody192/reflex-template/blob/main/Caddyfile)

    - Serves the exported frontend Reflex app
    - Proxies all requests to `/backend/*` through to the Reflex backend server

- **The `api_url` variable:** [rxconfig.py](https://github.com/brody192/reflex-template/blob/main/rxconfig.py)

    - Makes sure the frontend build utilizes the correct backend api url

**Relevant Caddy documentation:**

- [The Caddyfile](https://caddyserver.com/docs/caddyfile)
- [Caddyfile Directives](https://caddyserver.com/docs/caddyfile/directives)
- [reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [handle_errors](https://caddyserver.com/docs/caddyfile/directives/handle_errors)