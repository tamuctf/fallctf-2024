# TAMU Fall CTF 2024

Please read this document BEFORE contributing challenges. If your challenges do not conform to the standards defined here, they will not be merged until they are fixed.

## Contributing

As a development team, we like to keep our development process organized and easy to follow. The details here will help us keep the development process as painless as possible for both the developers and reviewers. 

For my sanity, please follow this document.

## Google Sheets

Google Sheets will be used to keep track of all challenges currently in development. There will be three tabs at the bottom of the sheet, two for challenges in FallCTF 2024 and TAMUctf 2025, and one to show all of the available cell options in each column.

You can find the spreadsheet here: https://docs.google.com/spreadsheets/d/1bOFMaldI793LTdE2KM9EYfJW8a86LRDRPL3FQDyiKy4/edit?usp=sharing

## Github

GitHub is the most critical platform used for managing challenge development. All code will be stored in this central repository. If you have not used Git or GitHub before, you can find a tutorial here: https://www.w3schools.com/git/

### Cloning

Please use SSH to clone the repository.

If you do not have an SSH key already:

1. `ssh-keygen -t ed25519`

2. You may use the default file name if you do not already have a default key.

3. Please set a passphrase for the key if you would like.

If you have an SSH key, but it is not linked to your GitHub:

1. Log in to https://github.com.

2. Go to https://github.com/settings/profile.

3. Select `SSH and GPG keys`.

4. Select `New SSH key`.

5. Add a title, select the `Authentication Key` type, and paste the PUBLIC key from the public-private key pair. DO NOT PASTE THE PRIVATE KEY.

If you already have an SSH key linked:

1. `git clone git@github.com:tamuctf/fallctf-2024.git`

2. `cd fallctf-2024`

If you have multiple keys and you would like to use a key other than the default one:

1. `GIT_SSH_COMMAND="ssh -i ~/.ssh/<key_name>" git clone git@github.com:tamuctf/fallctf-2024`

For anyone on Windows:

1. I am sorry for your loss.

2. Please use Windows Subsystem for Linux and follow the above instructions.

### Branching

For each new challenge, a new branch needs to be created. This will allow us to develop challenges at the same time without disturbing the main branch.

When creating a new challenge branch, please use the following naming convention:

- All lowercase

- Any spaces should use `-` (hyphen/dash/tac)

- Please do not use capital letters, underscores, or any other special characters (numbers are permitted).

Naming examples:

- `baked` - Good

- `first-restponder` - Good

- `shmooving-3` - Good

- `Baked` - Bad (Capital)

- `first_responder` - Bad (Underscore)

- `shmooving-3!` - Bad (Special character)

Commands:

1. `git branch <challenge-name>` - Create branch

2. `git checkout <challenge-name>` - Switch to branch

### Commits and Pushing to Remote

While developing, you will need to save your changes. Commits allow you to save changes in the repository. Pushing changes to remote sends a backup of your changes to the central repository. You may create as many commits and pushes as you like, but there are some general things you should keep in mind.

Making Good Commits:

- Commit messages should describe what changes have been made.

- Typically, commits should be made after feature(s) have been implemented rather than after every line of code.

Creating Commits:

1. Get current changes: (Modified and untracked files).

    `git status`

2. Add necessary files:

    `git add <file-name>`

Note: Do not commit binary files, virtual environment directories, or any potentially sensitive files. If you have questions about acceptable files, please ask.

3. Committing changes:

    `git commit -m <commit message>` - Make a commit with a short commit message.

    `git commit` - Make a commit with a long commit message (Opens a text editor).

Pushing Changes to Remote:

1. When working in your own branch, you should not have any interference, but you should make sure to pull before you push just in case.

    `git pull`

2. When making the first push to a new branch:

    `git push --set-upstream origin <branch name>`

3. When making any other push to the branch:

    `git push`

Handling potential merge conflicts:

If you receive a warning about merge conflicts, they will need to be resolved before proceeding. The CLI messages will be fairly verbose and instruct you on how to proceed. If you need help in the event of a merge conflict, please ask.

### Creating Pull Requests

When creating a pull request, it is best to do so on GitHub rather than in the CLI.

1. Go to the main repository page: https://github.com/tamuctf/fallctf-2024.

2. Click on the branch drop-down and select your branch.

3. Click on the contribute dropdown and select `Open pull request`.

4. Make the title the name of the challenge, and copy the README to the description. You may also add any other comments needed for the review process.

5. Add the correct category label.

6. Notify anybody who you would like to review the challenge.

### Challenge Review Process

All challenges will need to be reviewed before they can be merged into main.

The challenge review is separated into two phases

1. Initial challenge review

    - Add solution.

    - Verify that there is no cheese.

    - Author should verify solution and apply any necessary patches.

2. Infrastructure verification

    - The infrastructure team (Bode, et al.) verifies that the challenge conforms to the necessary standards.

    - If changes need to be made, they will be made either by the infrastructure team or the challenge author. If the author makes these changes they will need to verify with the infrastructure team again.

Once all reviews are completed the challenge may be merged.

## Magic

Developed by the sanest infra guy and one of the former devs, Magic is an automation tool built to make all of our lives much easier. Magic automates a lot of tedious infrastructure tasks and significantly reduces the headache of spinning up our infrastructure.

The repository can be found here: https://github.com/tamuctf/magic

### Installation

1. Install python 3.11

    `sudo add-apt-repository ppa:deadsnakes/ppa -y`

    `sudo apt install python3.11`

    `python3.11 --version`

    Note: `pyenv` can be used to manage versions.

2. Clone the repository

    `git clone git@github.com:tamuctf/magic.git`

    `cd magic`

3. Create a virtual environment

    `python3.11 -m venv venv`

    `source venv/bin/activate`

4. Install the package

    `pip install wheel`

    `pip install .`

The installation will only be accessible inside the virtual environment. It is recommended to use a virtual environment so you do not interfere with any of your other Python projects. Any time you want to use magic you must first activate the virtual environment as shown above.

### New Challenge

1. Navigate to the competition repository's root directory.

2. Create a new branch:

    `git branch <challenge-name>`

    `git checkout <challenge-name>`

3. Use magic to add the challenge:

    `magic challenge add --help`

    Note: if the `secrets.toml` file does not already exist run `cp secrets.toml.example secrets.toml`

    Select the flags needed for the challenge

    `magic challenge add <flags>`

Note: Please use the same naming convention for `<challenge-name>` as branch creation.

When a new challenge is created, Magic will copy several different baseline templates. Not all of these templates are necessary and are only initially included for your convenience. 

The following files are required by magic:

- `README.md`

- `config.toml`

- `Makefile` (Not required for challenges that are not hosted and do not have builds)

The standards and requirements for each of the files are listed below.

### `README.md` Standards

The default README.md file demonstrates how the file should be formatted.

Challenge Title:

- The challenge title at the top does not need to conform to any standard. This is what will be displayed on CTFd for competitors.

Challenge Description:

- The challenge description is given to the competitors in CTFd. Do not put any sensitive information in this area.

Development Notes and Solution sections:

- These areas do not need to be formatted in any special way. As long as every section after the description starts with `## <Section Name>`, it will not be parsed by the README parser.

Setting the Flag:

- The flag should be placed at the end of the README as shown in the template.

### `config.toml` Standards

Settings Section:

- The settings are fairly self-explanatory given the comments.

    - `deploy` should be set to true.

    - `containers` should be set to true if it is necessary to host docker containers for the challenge.

CTFd Section:

- This section can be removed for this competition. We will not be using static scoring.

Services Section:

- This section can be removed if docker containers do not need to be hosted.

- If docker containers must be hosted, then the public services must be defined here. The format for this is as follows:

```toml
[services.<service-name>]
port = <port>
type = <challenge-type>
```

- The service name should describe what the service is, such as `web`, `sql`, `uart`, or `socat`. Please use the same naming convention as git branches

- The port should be the same port that the challenge is being hosted on. This will be the port same port you define in your Makefile

- The type will either be `site` or `stream`:

    - `site` is used for web challenges or anything that requires a web interface.

    - `stream` is used for everything else.

Nginx Section:

- This section defines the specifications for load balancing. 

- Our standard number of instances is 5.

- The balance method will change based on the challenge type:

    - `least_conn` - Used for pwn challenges or any challenge that does not require the competitor to connect to the same instance.

    - `ip_hash` - Used for web challenges or any challenge that requires competitors to connect to the same instance. (Deprecated)

    - `hash $proxy_protocol_addr` - Replacement for `ip_hash`

### `Makefile` Standards

Common Rules:

- `all` - Execute all rules necessary to build and run the challenge, including distributables.

- `build` - Build binaries or docker containers.

- `run` - Run docker containers.

- `clean` - Stop containers and remove artifacts.

- `extract` - Build binaries inside docker and extract them to the local file system.

- `dist` - Prepare challenge distributables

Docker Compose:

Pretty please don't use docker-compose unless you absolutely have to. If you must, you can find the template at `Makefile.compose`.

- Variables:

    - `NAME` - Same as the branch name and challenge directory name.

    - `REGISTRY` - Leave empty.

    - `SUFFIX` - Leave empty.

    - `CPORTS` - Port(s) used by the challenge. These port(s) should match the service(s) defined in `config.toml`.

    - `HPORTS` - Do not change.

    - `SERVICES` - Service(s) used by the challenge. These service(s) should be the same as the service(s) defined in `config.toml`. Please use all caps and hyphens (-) only for these values.

    - `DOCKER_CONTEXT` - Leave this alone unless you need to change it.

    - `DOCKER_GLOBAL` - Leave this alone unless you need to change it.

    - `DOCKER_REGISTRY` - Do not change.

    - `PREFIX` - Define necessary variables that need to be passed to the docker-compose file as shown in the `Makefile.compose` template and the `docker-compose.yml` template.

- Running the challenge

    - `make build`

    - `make run`

- Stopping the challenge

    - `make stop`

Docker:

- Variables:

    - `NAME` - Same as the branch name and challenge directory name.

    - `REGISTRY` - Leave empty.

    - `SUFFIX` - Leave empty.

    - `CPORTS` - Port(s) used by the challenge. These port(s) should match the service(s) defined in `config.toml`.

    - `HPORTS` - Leave this alone.

    - `SERVICES` - Service(s) used by the challenge. These service(s) should be the same as the service(s) defined in `config.toml`. Please use all caps and hyphens (-) only for these values.

    - `DOCKER_CONTEXT` - Leave this alone unless you need to change it.

    - `DOCKER_GLOBAL` - Leave this alone unless you need to change it.

    - `DOCKER_RUNTIME` - This may need to be changed based on the needs of the challenge. The memory and cpu values may be changed within reason, and the read-only flag may be removed if writes need to occur during the challenge.

    - `CC` - Define the compiler if necessary.

    - `CFLAGS` - Define the compiler flags if necessary.

- Notes: 

    - If distributables are not needed, the `$(NAME)`, `extract`, and `dist` rules can be removed, and the `all` rule can be modified to call `run` or removed altogether.

    - When writing the `clean` rule, make sure to stop and remove the container using: `docker container rm -f $(NAME)$(SUFFIX)`

    - Make sure all build artifacts are removed when the `clean` rule is called.

    - The `run` rule should not call build.

Dist:

- Variables:

    - `NAME` - Same as the branch name and challenge directory name.

- Notes:

    - Make sure all build artifacts are removed when clean is called.

    - The distributable zip file should be named `<challenge-name>.zip`. Please verify this in testing.

    - Ensure that no sensitive files are accidentally included in the distributables. If you haven't heard, ask the old devs about Sacrifice.

### `solver-template.py` Standards

If your challenge requires competitors to connect to our infrastructure via SNI then a `solver-template.py` will need to be included. Essentially this means that any hosted challenge that is not a website will need to include the `solver-template.py` file in the challenge distributables even if the challenge is not sourced.

The solver template file only needs one change if it is needed. The `sni` parameter in the `remote()` function call should be changed to the name of the challenge that matches the name of the challenge's parent directory.

### Supported Challenge Types

Magic currently supports both Docker and Docker Compose, but please try to avoid using Docker Compose if you can.

If you have any questions about if a challenge can be supported by our infrastructure please contact Nathan or Bode.

## Development Considerations

This section is a list of considerations and recommendations from current and former developers for anyone to enjoy.

If you have anything to add here, feel free to open a pull request.

### Common Development Issues

- "Works on my machine". The reason we use docker is both for security and so we don't have the classic issue that every programmer runs into. However, sometimes even docker causes compatibility issues. If you run into this issue, work with other devs to try to find a solution to make the challenge more stable.

### Infrastructure

- Do not let competitors get RCE on a box that allows writes. All challenge containers should be read-only unless absolutely necessary.
