'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const errors = [];

function assert(condition, message) {
  if (!condition) {
    errors.push(message);
  }
}

function read(file) {
  return fs.readFileSync(path.join(root, file), 'utf8');
}

const requiredFiles = [
  'index.html',
  'style.css',
  'script.js',
  'faq.css',
  'faq.js',
  'galleria.css',
  'galleria.js',
];

for (const file of requiredFiles) {
  assert(fs.existsSync(path.join(root, file)), `Missing required file: ${file}`);
}

const html = read('index.html');

assert(html.includes('class="contact-section"'), 'Contact section is missing');
assert(html.includes('id="contatti"'), 'Contact anchor is missing');
assert(html.includes('Vieni a trovarci e a conoscerci'), 'Contact eyebrow copy is missing');
assert(html.includes('contact-visit-steps'), 'Visit journey block is missing');
assert(html.includes('contact-reassurance'), 'Reassurance quote is missing');
assert(html.includes('tel:+393762031211'), 'Phone link is missing');
assert(html.includes('Prenota una visita'), 'Primary CTA is missing');

const css = read('style.css');
assert(css.includes('.contact-visit-step'), 'Visit step styles are missing');
assert(css.includes('.contact-reassurance'), 'Reassurance styles are missing');

if (errors.length > 0) {
  console.error('Site validation failed:\n');
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log('Site validation passed.');
