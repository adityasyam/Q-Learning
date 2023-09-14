# Setup

## Installing Docker

### MacOS

1. If not already installed, install [Homebrew](https://brew.sh/), a package
   manager for MacOS and Linux
2. Install Docker

   ```text
   brew install --cask docker
   ```

3. Open the newly installed _Docker Desktop_ application
   1. You should be able to find it in the application folder
   2. Otherwise, use Spotlight search (<kbd>⌘</kbd> + <kbd>space</kbd>) and
      search for "Docker"
4. Select "Use recommended settings"
5. Skip remaining steps if possible

### Linux

1. See [Docker install documentation](https://docs.docker.com/engine/install/)
   (ask Ari)

### Windows

1. See [Docker install documentation](https://docs.docker.com/engine/install/)
   (untested)

## Running Docker

1. Set your working directory to the top level of the Q-learning repository
2. Running commands:

   ```text
   docker-compose run --rm nav [COMMANDS]
   ```

   1. This command will create an image and container (if necessary) and execute
      the given commands
   2. The `--rm` option deletes the container that was created to run the
      commands on exit
   3. Example: `docker-compose run --rm nav python main.py` will run main.py 🙂

## Tips

1. Create an alias in your `.bashrc` (or whatever shell you are using) to avoid
   getting carpal tunnel

   ```bash
   alias nav='docker-compose run nav --rm'
   ```

   A quick way to do this if you are using Bash

   ```text
   echo "alias nav='docker-compose run --rm nav'" >> ~/.bashrc
   ```

   Or Zsh (default on MacOS)

   ```text
   echo "alias nav='docker-compose run --rm nav'" >> ~/.zshrc
   ```

2. The working directory of the navigation image (defined in
   `Dockerfile-navigation`) is set to `/usr/app`, which is bound as a volume to
   the entire Q-learning repository stored locally on the host (this way code
   changes do not require new image build, see `docker-compose.yml`)

   If you are working primarily in a specific module, it can be helpful to set
   your working directory to something else, e.g.

   ```text
   docker-compose run --rm --workdir /usr/app/src/state_pred/ nav python sim.py
   ```

## X11 Forwarding

### MacOS

1. Install [XQuartz](https://www.xquartz.org/) via Homebrew

   ```text
   brew install --cask xquartz
   ```

2. Logout and login of your Mac to activate XQuartz as default X11 server
3. Open XQuartz

   ```text
   open -a XQuartz
   ```

4. Go to Security Settings (Menu Bar -> XQuartz -> Settings -> Security Settings)
   and ensure that "Allow connections from network clients" is on
5. Restart your laptop (FIXME: this step may not be necessary?)
6. Allow X11 forwarding from localhost via xhost

   ```text
   xhost + localhost
   ```

   **Important:** this must be run in the xterm window opened by default by
   XQuartz _every time_ XQuartz is started

7. Add the following option whenever you run `docker-compose run`:

   ```text
   --env DISPLAY=host.docker.internal:0
   ```

   Example:

   ```text
   docker-compose run --rm --env DISPLAY=host.docker.internal:0 nav python state_pred/sim.py
   ```

### Linux

In _theory_ this should be easier as most distros already use Xwindows,
but I know for a fact that the steps differ compared to Mac.

May have to bind this volume:

```text
--volume="$HOME/.Xauthority:/root/.Xauthority:rw"
```

May have to set

```text
--net=host
```

or

```text
--add-host=host.docker.internal:host-gateway
```

May have to bind x11 socket:

```text
--volume /tmp/.X11-unix:/tmp/.X11-unix
```

May have to set DISPLAY to

`--env DISPLAY=unix$DISPLAY` or `--env DISPLAY=$DISPLAY`

I'm not sure. Stack Overflow has a sea of possibilities.

May the odds be ever in your favor...

### Windows

No clue.