var express  = require('express'),
    app      = express(),
    subapp   = express(),
    swagger  = require('swagger-node-express');

var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var methodOverride = require('express-method-override');
var session = require('express-session');

var passport       = require('passport'),
    GitHubStrategy = require('passport-github').Strategy;


var config = {
    'OAUTH_ID': '1234',
    'OAUTH_TOKEN': '1234',
    'SESSION_TOKEN': 'abcde'
};



subapp.use(bodyParser.json());
subapp.use(bodyParser.urlencoded({extended: false}));
subapp.use(cookieParser());
subapp.use(methodOverride());
subapp.use(session({ secret: config['SESSION_TOKEN'], resave: false }));
subapp.use(passport.initialize());
subapp.use(passport.session());
//subapp.use(authenticate);
swagger.setAppHandler(subapp);


app.use(cookieParser());
app.use(bodyParser.urlencoded({extended: false}));
app.use(methodOverride());
app.use(session({ secret: config['SESSION_TOKEN'], resave: false }));
app.use(passport.initialize());
app.use(passport.session());
app.use(app.router);
//app.use(authenticate);
app.use('/api', subapp);
app.use('/swagger', function(req, res, next) {
    if (req.url === '/swagger') {
        res.redirect('/swagger/');
    }
    next();
});
app.use('/swagger', express.static(path.join(__dirname, 'public/swagger')));
app.use(express.static(path.join(__dirname, 'public/client')));


app.listen(1337);

/*
passport.use(new GitHubStrategy({
    clientID: config['OAUTH_ID'],
    clientSecret: config['OAUTH_TOKEN'],
    callbackURL: '/auth/github/callback'
}, function(accessToken, refreshToken, profile, done) {
    var user = {
        id: profile.username,
        email: (profile.emails.length) ? profile.emails[0].value : null,
        gravatar: profile._json.gravatar_id
    };
    return done(null, user);
}));


passport.serializeUser(function(user, done) {
  done(null, user);
});


passport.deserializeUser(function(user, done) {
  done(null, user);
});


// middleware to ensure user is authenticated
function authenticate(req, res, next) {
  if (req.isAuthenticated()) {
    return next();
  }
  if (req.headers['x-requested-with'] === 'XMLHttpRequest') {
    res.send("Authentication required", 401);
  } else {
    res.redirect('/login');
  }
}
*/


// configure express to use swagger for the `/api` route
/*
subapp.configure(function() {
});
*/


// configure express for the static content on the `/` route
/*
app.configure(function() {
});
*/


// GitHub OAuth routes
/*
app.get('/login', passport.authenticate('github'));
app.get('/auth/github/callback',  passport.authenticate('github', { successReturnToOrRedirect: '/', failureRedirect: '/login' }));


// Swagger configuration
swagger.addModels(require('./models'));
//swagger.addGet(require('./controllers/user').get);
swagger.configureSwaggerPaths('', '/doc', '');
swagger.configure('', require('./package.json').version);
*/
