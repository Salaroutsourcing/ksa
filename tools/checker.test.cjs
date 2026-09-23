const { test } = require('node:test');
const assert = require('node:assert/strict');
const { choices, clean, assess } = require('../assets/js/checker.js');
test('all 90 combinations return preparation guidance without promises or restricted offers', () => {
  let count = 0;
  for (const document of choices.document) for (const destination of choices.destination) for (const issue of choices.issue) {
    const steps = assess({ document, destination, issue });
    assert.ok(steps.length >= 4);
    assert.ok(steps.every(s => s.title && s.text));
    assert.doesNotMatch(JSON.stringify(steps), /\b(?:HEC|IBCC|MOFA|apostille|guaranteed approval)\b/i);
    assert.match(steps.at(-2).text, /Applicant-only/);
    count++;
  }
  assert.equal(count, 90);
});
test('handoff whitelists answers and discards arbitrary fields', () => {
  assert.deepEqual(clean({ document: '<script>', destination: 'Saudi Arabia', issue: 'Missing record', passport: 'private', email: 'private' }), { destination: 'Saudi Arabia', issue: 'Missing record' });
  assert.throws(() => assess({}), /Complete all three/);
});
test('record differences are addressed before process selection', () => {
  const steps = assess({ document: 'Degree / transcript', destination: 'Saudi Arabia', issue: 'Name or identity difference' });
  assert.equal(steps[0].title, 'Compare the records first');
  assert.match(steps[0].text, /Do not alter/);
});
test('unknown documents and destinations are not assumed academic or Saudi', () => {
  const steps = assess({ document: 'Other / not sure', destination: 'Other / not sure', issue: 'No known issue' });
  assert.match(steps[0].text, /should not be treated as an academic/);
  assert.match(steps[1].text, /Identify the specific country/);
});
