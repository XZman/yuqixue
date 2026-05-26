---
title: ''
summary: ''
date: 2025-05-16
type: landing

design:
  spacing: '5rem'

sections:
  - block: resume-biography-3
    id: about
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/yuqixue_cv.pdf
        date: May 2026
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle
  - block: publications-grouped
    id: papers
    content:
      title: Publications
      folder: publications
      groups:
        - title: Hardware/Software Co-design for NPU Ecosystem
          tag: NPU Co-design
        - title: ML Compiler for Inter-core Connected AI Chips
          tag: AI Compiler
          collapsed: true
        - title: Memory and Storage for AI Accelerators
          tag: AI Memory and Storage
          collapsed: true
        - title: Other Publications
          tag: Other Publications
          collapsed: true
  - block: resume-service
    id: experience
    content:
      title: Service
      username: me
    design:
      spacing:
        padding: ['1.5rem', 0, '1.5rem', 0]
  - block: resume-awards
    content:
      title: Awards
      username: me
    design:
      spacing:
        padding: ['1.5rem', 0, '1.5rem', 0]
  - block: resume-education
    content:
      username: me
    design:
      spacing:
        padding: ['1.5rem', 0, '1.5rem', 0]
  - block: resume-experience
    content:
      username: me
    design:
      date_format: 'January 2006'
      spacing:
        padding: ['1.5rem', 0, '1.5rem', 0]
  - block: resume-teaching
    content:
      title: Teaching
      username: me
    design:
      spacing:
        padding: ['1.5rem', 0, '1.5rem', 0]
---
