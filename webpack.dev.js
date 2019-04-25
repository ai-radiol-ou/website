const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist'
  }
});

htmls = ejss.map(name => {
    return new HtmlWebpackPlugin(
        {
            filename: name+'.html',
            template: 'src/'+name+'.ejs',
        }
    )
})

Array.prototype.push.apply(module.exports.plugins, htmls);
