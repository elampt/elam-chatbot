# Three Step Process
1. **Tool :** Take notes in Obsidian in **Markdown** language
2. **Conversion :** Use a tool that converts **Markdown** to HTML so that it can be displayed properly in a **Static Web** page (**Quarts** in my case)
3. **Hosting :** Take either paid services or go with **GitHub** to start with

# Updating the Site after Setup
## Key commands
* **Building the quartz**
	This will start a local web server to run our Quartz on our computer. We can view it at http://localhost:8080/

 `npx quartz build --serve`

* **Sync the change to Github & Deploy**
	Run this command every time we want to push updates to our repository.

`npx quartz sync`

* **Upgrading Quartz**
	To fetch the latest Quartz updates, simply run

`npx quartz update`

For more details, refer [Quartz 4.0](https://quartz.jzhao.xyz/) official documentation