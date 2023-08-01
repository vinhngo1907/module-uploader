const jwt = require("jwt-decode");
const axios = require("axios");
const { serverUrl, auth0Domain, clientId, redirectUri } = require("../configs");

let accessToken = null;
let profile = null;
let refreshToken = null;

function getAccessToken() {
    return accessToken;
}

function getProfile() {
    return profile;
}

function getAuthentication() {
    return (
        auth0Domain +
        "/authorize?" +
        "scope=openid profile offline_access&" +
        "response_type=code&" +
        "client_id=" +
        clientId +
        "&" +
        "redirect_uri=" +
        redirectUri
    )
}

async function refreshTokens() {
    if (refreshToken) {
        const refreshOptions = {
            method: "POST",
            url: `${auth0Domain}/oauth/token`,
            headers: { "content-type": "application/json" },
            data: {
                grant_type: "refresh_token",
                client_id: clientId,
                refresh_token: refreshToken
            }
        }
        try {
            const response = await axios(refreshOptions);
            accessToken = response.data.access_token;
        } catch (error) {
            window.location.href("/logout");
            throw error;
        }
    } else {
        throw new Error("No available refresh token.");
    }
}

async function loadTokens(callbackURL) {
    const urlParts = url.parse(callbackURL, true);
    const query = urlParts.query;

    const exchangeOptions = {
        grant_type: "authorization_code",
        client_id: clientId,
        code: query.code,
        redirect_uri: redirectUri
    };

    const options = {
        method: "POST",
        url: `${auth0Domain}/oauth/token`,
        headers: { "content-type": "application/json" },
        data: JSON.stringify(exchangeOptions)
    };

    try {
        const response = await axios(options);
        accessToken = response.data.access_token;
        refreshToken = response.data.refresh_token;

        if (refreshToken) {
            //   await keytar.setPassword(keytarService, keytarAccount, refreshToken);
        }

    } catch (error) {
        window.location.href = "/logout"
        throw error;
    }
}

function setCookie()

module.exports = {
    refreshToken,
    getAccessToken
}