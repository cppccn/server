const gulp = require('gulp');
const ts = require('gulp-typescript');
const JSON_FILES = ['src/*.json', 'src/**/*.json'];

// pull in the project TypeScript config
const tsProject = ts.createProject('tsconfig.json');

gulp.task('scripts', function() {
  const tsResult = tsProject.src()
    .pipe(tsProject());
  return tsResult.js.pipe(gulp.dest('dist'));
});

gulp.task('watch', gulp.parallel('scripts', function() {
  gulp.watch('src/**/*.ts', gulp.parallel('scripts'));
}));

gulp.task('assets', function() {
  return gulp.src(JSON_FILES)
    .pipe(gulp.dest('dist'));
});

gulp.task('default', gulp.parallel(['watch', 'assets']));

var typedoc = require("gulp-typedoc");
gulp.task("typedoc", function() {
  return gulp
    .src(["src/**/*.ts"])
    .pipe(typedoc({
      module: "commonjs",
      target: "es5",
      out: "docs/",
      name: "CappuccinoServer"
    }))
  ;
});
