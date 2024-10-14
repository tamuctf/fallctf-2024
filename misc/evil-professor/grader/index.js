const express = require('express');
const cors = require('cors')
const crypto = require('crypto')
const { spawn } = require('child_process');

const app = express();
const port = 5000;
const executionTime = 5000;
const flag = 'gigem{d0n7_d0_7hi5_0n_y0ur_4c7u41_455i9nm3n75}';

const tests = [
    '108992dc427ebac46d6fb6fef302bf93b05f38442a16a0d162cf7c4634549fc3',
    '802c8aa0610684aeb90a2bd3abc4541b12cab6b69c99ff1ec74da96352a23424',
    '3d38b3c55f1d4c840a44ab4890b805c3a4278fa7372122ae2323281495b9b43e'
];

app.use(cors());
app.use(express.json());

app.post('/test-code', (req, res) => {
    if (!req.body.code)
        return res.status(400).send({ error: 'Missing code' });
    
    let code = req.body.code;
    
    code += '\n'
    tests.forEach(test => {
        code += `print(reverse_sha256('${test}'))\n`
    });

    const process = spawn('sudo', ['-u', 'grader', 'python3', '-c', code]);
    
    let timedOut = false;
    let output = '';
    let error = '';

    process.stdout.on('data', data => {
        output += data.toString();
    });

    process.stderr.on('data', data => {
        error += data.toString();
    });

    const timeout = setTimeout(() => {
        process.kill('SIGTERM');
        timedOut = true;
        res.status(500).send({ error: 'Execution timed out' });
    }, executionTime)

    process.on('close', code => {
        clearTimeout(timeout);

        if (!timedOut) {
            if (code !== 0)
                return res.status(500).send({ error: error });

            let lines = output.split('\n');

            if (lines.length !== 4)
                return res.status(400).send({ error: 'Invalid code output'});

            let results = {}
            lines.pop();

            lines.forEach((line, idx) => {
                line += '\n';
                let hash = crypto.createHash('sha256').update(line).digest('hex');
                results[`Test ${idx + 1}`] = tests[idx] !== hash ? 'Fail' : 'Success';
            });

            if (!(JSON.stringify(results).includes('Fail')))
                results['Flag'] = flag;

            return res.status(200).send(results);
        }
    });
});

app.listen(port, '127.0.0.1');
