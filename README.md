# Open Gateway's developers website content repository

This repository is the source of content to the Open Gateway's developers website. Each page in the website must be linked to a markdown file in this repository and will get updated and published as the result of a pull request for every change.

Visit [developers.opengateway.telefonica.com](https://developers.opengateway.telefonica.com)

## Table of contents
The contents in this repo are meant to be organized in the following structure and order. Folding and sorting to be set by the Readme.com site admin in the website configuration:

- About Open Gateway
	- [The Open Gateway Initiative](about/initiative.md)
	- [API Architecture](about/architecture.md)
	- [CAMARA project](about/camara.md)
	- [Privacy by Design](about/privacy.md)
	- [Glossary of Terms](about/glossary.md)
- Getting Started
	- [Join our Programs](gettingstarted/programs.md)
	- [Sandbox](gettingstarted/sandbox/sandbox.md)
		- [Sandbox SDK reference](gettingstarted/sandbox/sdkreference.md)
- API Call Flows
	- [API Integration](callflows/apiintegration.md)
	- [Authorization](callflows/authorization/authorization.md)
		- [Frontend flow](callflows/authorization/frontend.md)
		- [Backend flow](callflows/authorization/backend.md)
- API Catalog
	- [Available APIs](catalog/available.md)
		- [SIM Swap](catalog/simswap/simswap.md)
		- [Number Verification](catalog/numberverification/numberverification.md)
		- For each API available on our Sandbox or on any Channel Partner (see above):
			- About the API
			- API reference on Readme.com
			- Sample code
				- HTTP integration
				- Using the Sandbox SDK
					- Using a generic Channel Partner SDK (alternative CTA)
				- Open-source comprehensive sample application (GitHub repo)
	- [API Roadmap](catalog/roadmap.md)
		- For every API not yet commercially available:
			- Link to the API documentation on the Open Gateway website
			- Link to the API reference on CAMARA's GitHub repository

## How to contribute
- [ ] Clone this repository
- [ ] Create a new branch called `your-name/the-change`
- [ ] Make the changes into your own branch
- [ ] Create a pull request to the `main` branch
- [ ] Add main contributors as reviewers to the pull request
	
	- [ ] Laura Lacarra [@lauralacarraarcos](https://github.com/lauralacarraarcos) (Go to Developer)
	- [ ] Agustín Martín [@amg77](https://github.com/amg77) (Global Product)
	- [ ] Diego Rivera [@diegotid](https://github.com/diegotid) (Global Product)
	- [ ] Teresa B. Lufuluabo [@lufuOGW](https://github.com/lufuOGW) (Go to Developer)

## How to publish to the website
- [ ] Include the Readme.com front matter to each markdown file
- [ ] Wait for the pull request to be approved
- [ ] Merge the pull request to the `main` branch, this will trigger the website update
