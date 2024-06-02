'use client';
import React from 'react';

interface CodeOutputProps {
    output: string
}

const CodeOutput: React.FC<CodeOutputProps> = ({ output }) => (
    <div>
        <h3 className="text-xl font-bold mb-4 text-green-500 flex justify-start">Output</h3>
        <div className='bg-white h-52' >
            {output && <pre className="mt-4 p-2 text-black">{output}</pre>}
        </div>
    </div>
)

export default CodeOutput