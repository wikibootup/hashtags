module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    qunit: {
      files: ['**/tests/**/*.html']
    },

    watch: {
      tasks: ['qunit']
    }
  });

  grunt.registerTask('test', ['qunit']);

  grunt.loadNpmTasks('grunt-contrib-qunit');

  // Default task(s).
  grunt.registerTask('default', []);

};
