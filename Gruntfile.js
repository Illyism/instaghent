module.exports = function(grunt) {
  grunt.initConfig({
    less: {
      options: {
        compress: true,
        report: "min"
      },
      dev: {
        src: ['src/less/style.less'],
        dest: 'server/static/css/style.css'
      }
    },
    watch: {
      less: {
        files: ['src/less/*'],
        tasks: ['less'],
      },
      livereload: {
        options: { livereload: true },
        files: ['server/static/css/*', "server/templates/**", "server/static/js/*"],
      },
    },
  });

  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.registerTask('default', ["less", 'watch']);
};