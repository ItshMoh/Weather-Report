# Weather-Report
This is a Project that utilizes the AsyncAPI templates to generate code to know weather of a location.

## Run the Program Locally
1. Fork and clone the Repo.
2. Run npm i command in the terminal.
2. Go into the test/project/config.py file and Paste the Weather API KEY. You can get it from weatherapi.com
3. Now delete the test/project/client.py file. It will be regenerated using generator.
4. In the Terminal run  command 'asyncapi generate fromTemplate ./test/fixtures/asyncapi.yml ./ -o test/project --force-write -p server=dev'. 
5. A client.py file will be formed in the test/project folder.
6. Now run the command 'python test/project/cli.py' in the terminal
7. You will get prompt to enter the location of which you want to know the weather details.
8. After entering the location  you will get the weather details.

For More information about the Templates and Generator go to https://www.asyncapi.com/docs/tools/generator/generator-template .