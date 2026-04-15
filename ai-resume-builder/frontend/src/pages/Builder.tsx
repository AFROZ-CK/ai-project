import React, { useState, useCallback } from 'react';
import { useMutation } from '@tanstack/react-query';
import { ResumeForm } from '../components/ResumeForm';
import { ResumePreview } from '../components/ResumePreview';
import { AIAssistant } from '../components/AIAssistant';
import { ExportPanel } from '../components/ExportPanel';
import { generateResume, optimizeForJob } from '../utils/api';
import type { ResumeData, GenerateResumePayload } from '../types/resume';

const Builder: React.FC = () => {
  const [resumeData, setResumeData] = useState<ResumeData | null>(null);
  const [activePanel, setActivePanel] = useState<'form' | 'ai' | 'export'>('form');
  const [selectedTemplate, setSelectedTemplate] = useState('modern');
  const [jobDescription, setJobDescription] = useState('');

  const generateMutation = useMutation({
    mutationFn: (payload: GenerateResumePayload) => generateResume(payload),
    onSuccess: (data) => {
      setResumeData(data);
      setActivePanel('export');
    }
  });

  const optimizeMutation = useMutation({
    mutationFn: ({ resumeId, jd }: { resumeId: string; jd: string }) =>
      optimizeForJob(resumeId, jd),
    onSuccess: (data) => {
      console.log('Optimization suggestions:', data);
    }
  });

  const handleGenerate = useCallback((formData: GenerateResumePayload) => {
    generateMutation.mutate({ ...formData, template: selectedTemplate });
  }, [generateMutation, selectedTemplate]);

  const handleOptimize = useCallback(() => {
    if (!resumeData?.id || !jobDescription) return;
    optimizeMutation.mutate({ resumeId: resumeData.id, jd: jobDescription });
  }, [resumeData, jobDescription, optimizeMutation]);

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Left Panel - Controls */}
      <div className="w-1/2 bg-white border-r border-gray-200 flex flex-col">
        {/* Panel Tabs */}
        <div className="flex border-b border-gray-200">
          {(['form', 'ai', 'export'] as const).map((panel) => (
            <button
              key={panel}
              onClick={() => setActivePanel(panel)}
              className={`flex-1 py-3 text-sm font-medium capitalize transition-colors ${
                activePanel === panel
                  ? 'text-purple-600 border-b-2 border-purple-600'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              {panel === 'ai' ? '🤖 AI Assistant' : panel === 'form' ? '📝 Edit' : '📤 Export'}
            </button>
          ))}
        </div>

        {/* Panel Content */}
        <div className="flex-1 overflow-y-auto p-6">
          {activePanel === 'form' && (
            <ResumeForm
              onSubmit={handleGenerate}
              isLoading={generateMutation.isPending}
            />
          )}
          {activePanel === 'ai' && (
            <AIAssistant
              resumeData={resumeData}
              jobDescription={jobDescription}
              onJobDescriptionChange={setJobDescription}
              onOptimize={handleOptimize}
              isOptimizing={optimizeMutation.isPending}
              optimizationResult={optimizeMutation.data}
            />
          )}
          {activePanel === 'export' && (
            <ExportPanel
              resumeData={resumeData}
              selectedTemplate={selectedTemplate}
              onTemplateChange={setSelectedTemplate}
            />
          )}
        </div>
      </div>

      {/* Right Panel - Preview */}
      <div className="w-1/2 bg-gray-100 flex flex-col">
        <div className="bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between">
          <span className="text-sm font-medium text-gray-600">Live Preview</span>
          <div className="flex items-center gap-2">
            <span className="text-xs text-gray-400">Template:</span>
            <select
              value={selectedTemplate}
              onChange={(e) => setSelectedTemplate(e.target.value)}
              className="text-xs border border-gray-200 rounded px-2 py-1"
            >
              <option value="modern">Modern</option>
              <option value="classic">Classic</option>
              <option value="minimal">Minimal</option>
              <option value="creative">Creative</option>
              <option value="executive">Executive</option>
            </select>
          </div>
        </div>
        <div className="flex-1 overflow-y-auto p-6">
          {resumeData ? (
            <ResumePreview data={resumeData} template={selectedTemplate} />
          ) : (
            <div className="flex items-center justify-center h-full text-gray-400">
              <div className="text-center">
                <div className="text-6xl mb-4">📄</div>
                <p className="text-lg font-medium">Fill in your details</p>
                <p className="text-sm">Your AI-generated resume will appear here</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Builder;

// Updated: 2026-11-19T21:09:00

// Updated: 2026-09-02T14:25:00

// Updated: 2026-09-19T21:07:00

// Updated: 2026-08-08T18:54:00

// Updated: 2026-10-01T09:56:00

// Updated: 2026-06-03T09:29:00

// Updated: 2026-10-01T13:03:00

// Updated: 2026-06-21T20:53:00

// Updated: 2026-07-26T12:39:00

// 2026-05-21 10:00

// 2026-05-22 11:00

// 2026-05-23 09:00

// 2026-05-26 10:30

// 2026-05-27 09:00

// 2026-05-28 11:00

// 2026-06-06 09:00

// 2026-06-13 09:30

// 2026-06-17 11:00

// 2026-06-20 09:00

// 2026-07-02 11:00

// 2026-07-07 10:00

// 2026-07-10 10:00

// 2026-07-16 09:00
