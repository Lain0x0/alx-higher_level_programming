#!/usr/bin/node
const fs = require('fs');

const Filearg = fs.readFileSync(process.argv[2]).toString();
const Sarg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], Filearg + Sarg);
