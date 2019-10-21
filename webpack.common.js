const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'js/main.js'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            'css-loader',
            'sass-loader',
          ]
        })
      },
      {
        test: /\.ejs$/,
        use: 'ejs-compiled-loader'
      },
    ]
  },
  plugins: [
    new ExtractTextPlugin('css/styles.css'),
  ]
};

ejss = ['index', 'people', 'research', 'links', '404',
        'optout/index', 'optout/201909']
