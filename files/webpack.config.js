const HtmlWebPackPlugin = require('html-webpack-plugin');
const webpack = require("webpack");
const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    path: path. resolve(__dirname, './static/frontend/build'),
    filename: '[name].js',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      },
      {
        test: /\.s?css$/i,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.(png|svg|jpg|gif|svg)$/i,
        loader: 'file-loader',
      },
    ],
  },
    // Needed to use JSX file extension
  resolve : {
    extensions : ['.js', '.jsx']
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    // Used for [ webpack-dev-server ] to auto-refresh page as normal React project.
    new HtmlWebPackPlugin({
      template: './src/index.html',
      filename: './index.html'
    }),
    // This has effect on React Library Size ( no change observed )
    new webpack.DefinePlugin({
      "process.env": {
        "process.env.NODE_ENV": JSON.stringify("production"),
      },
    }),
  ],
  devServer: {  
    historyApiFallback: true,
  },
}