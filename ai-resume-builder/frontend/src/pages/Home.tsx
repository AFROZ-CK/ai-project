import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '../components/ui/Button';
import { Hero } from '../components/Hero';
import { Features } from '../components/Features';
import { TemplateShowcase } from '../components/TemplateShowcase';
import { Testimonials } from '../components/Testimonials';

const Home: React.FC = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  const handleGetStarted = () => {
    navigate('/builder');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <nav className="fixed top-0 w-full z-50 bg-black/20 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-400 to-pink-400 rounded-lg" />
              <span className="text-white font-bold text-xl">ResumeAI</span>
            </div>
            <div className="hidden md:flex items-center gap-6">
              <a href="#features" className="text-gray-300 hover:text-white transition-colors">Features</a>
              <a href="#templates" className="text-gray-300 hover:text-white transition-colors">Templates</a>
              <a href="#pricing" className="text-gray-300 hover:text-white transition-colors">Pricing</a>
            </div>
            <div className="flex items-center gap-3">
              <Button variant="ghost" onClick={() => navigate('/login')}>Login</Button>
              <Button variant="primary" onClick={handleGetStarted}>Get Started Free</Button>
            </div>
          </div>
        </div>
      </nav>

      <Hero onGetStarted={handleGetStarted} />
      <Features />
      <TemplateShowcase />
      <Testimonials />

      <footer className="bg-black/40 border-t border-white/10 py-12">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-gray-400">
            © 2024 ResumeAI. Built with ❤️ using GPT-4 and React.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Home;

// Updated: 2026-09-19T21:08:00

// Updated: 2026-08-05T09:13:00

// Updated: 2026-11-21T17:55:00

// Updated: 2026-06-24T18:17:00

// Updated: 2026-07-14T13:57:00

// Updated: 2026-11-23T13:51:00

// Updated: 2026-09-09T19:00:00

// Updated: 2026-07-08T17:08:00

// 2026-05-20 09:30

// 2026-06-18 09:30

// 2026-06-19 10:00

// 2026-07-11 09:00
