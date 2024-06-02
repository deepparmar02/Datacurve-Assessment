'use client';
import React, { useState } from 'react';
import CodeEditor from '@monaco-editor/react';
import AppButton from '../components/AppButton';
import { submitCode, testCode } from '../utils/api';
import CodeOutput from '../components/CodeOutput';

const CodeEditorPage: React.FC = () => {
    const [code, setCode] = useState<string>('');
    const [output, setOutput] = useState<string>('');

    const handleTestCode = async () => {
        try {
            const result = await testCode(code);
            setOutput(result);
        } catch (error: any) {
            setOutput(`Error: ${error.response?.data?.detail || error.message}`);
        }
    };

    const handleSubmit = async () => {
        try {
            const result = await submitCode(code);
            setOutput(result);
        } catch (error: any) {
            setOutput(`Error: ${error.response?.data?.detail || error.message}`);
        }
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4 text-green-500 flex justify-center">Python Code Executor</h1>
            <CodeEditor
                height="50vh"
                language="python"
                value={code}
                defaultValue="# Start coding here"
                onChange={(value) => setCode(value || '')}
            />
            <div className="my-4 flex justify-center gap-4">
                <AppButton handleClick={handleTestCode} title='Test Code' />
                <AppButton handleClick={handleSubmit} title='Submit' />
            </div>
            <CodeOutput output={output}/>
        </div>
    );
};

export default CodeEditorPage;