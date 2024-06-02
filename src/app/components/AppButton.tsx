'use client';
import React from 'react';

interface AppButtonProps {
    handleClick: any,
    title: string
}

const AppButton: React.FC<AppButtonProps> = ({ handleClick, title }) => (
    <button className="btn btn-primary px-2 mr-2 text-lg font-bold text-white rounded bg-green-500 hover:bg-green-700" onClick={handleClick}>{title}</button>
)

export default AppButton