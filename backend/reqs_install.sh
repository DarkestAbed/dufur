# Debian 11+ / Ubuntu 22.04+
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg
curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | sudo gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | sudo tee /etc/apt/sources.list.d/doppler-cli.list
sudo apt update 
sudo apt install doppler

# checking doppler
doppler --version > /dev/null
if [ $? == "0" ]
    then
        doppler login
    else
        echo "Error instalando Doppler. Revisa y reintenta."
        exit 11
fi

# authorizing project
if [ -f "$(pwd)/doppler.yaml" ]
    then
        echo "Doppler config found."
    else
        touch $(pwd)/doppler.yaml
        echo "setup:\n\t- project: dufur\n\t  config:dev\n" > $(pwd)/doppler.yaml
fi
doppler setup

# wrap
echo "All done!"
