Step 1 — Install Docker Desktop

Go to https://www.docker.com/products/docker-desktop/ and download the Windows installer. Run it, let it finish, then restart your machine when it asks (this part is mandatory — Docker needs WSL2 to be initialized).

After restart, open Docker Desktop and wait for it to say "Engine running" in the bottom left. That's the only sign you need.

Step 2 — Verify it works

Open PowerShell and run:

powershelldocker --version

You should see something like Docker version 27.x.x. If that prints, you're good.

Step 3 — Run n8n

Once Docker is confirmed working, run this single command in PowerShell:

powershelldocker run -it --rm -p 5678:5678 -v n8n\_data:/home/node/.n8n n8nio/n8n

What this does, briefly: docker run pulls and starts the n8n container, -p 5678:5678 exposes it on your localhost, and -v n8n\_data:/home/node/.n8n creates a named volume so your workflows are saved even after you stop the container. The --rm flag cleans up the container on exit but the volume persists — so your work is safe.

First run will take a minute to pull the image. Once you see something like Editor is now accessible via: http://localhost:5678, open that URL in your browser.

