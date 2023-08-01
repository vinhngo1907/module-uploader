const dotenv = require("dotenv");
dotenv.config();

module.exports = {
    "auth0Domain": process.env.AUTH0_DOMAIN,
    "clientId": process.env.CLIENT_ID,
    "apiIdentifier": process.env.API_IDENTIFIER,
    "redirectUri": process.env.REDIRECT_URI,
    "serverUrl": process.env.SERVER_URL,
    "clientSecret": process.env.CLIENT_SECRET,
    "port": process.env.PORT
}