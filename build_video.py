import os
import sys
import time
import wave
import subprocess
import win32com.client
import imageio_ffmpeg

def generate_video():
    base_dir = r"c:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship"
    pptx_path = os.path.join(base_dir, r"ShadowFox_Internship_Documentation\Presentation\ShadowFox_Data_Analyst_Internship_Presentation.pptx")
    temp_dir = os.path.join(base_dir, "temp_video_build")
    os.makedirs(temp_dir, exist_ok=True)
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"Using FFmpeg: {ffmpeg_exe}")

    # 1. Slide Narration Scripts (Timed for 3.5 - 4.0 minutes total)
    narrations = [
        # Slide 1: Title
        "Hello everyone. My name is Keerthana V, Data Analyst Intern at ShadowFox, from HKBK College of Engineering. "
        "Today, I am proud to present the complete capstone portfolio for my ShadowFox Data Analyst Internship.",

        # Slide 2: Contents
        "This presentation covers the formal acknowledgement, followed by comprehensive deep dives into all three project levels: "
        "the Beginner sales analysis, the Intermediate customer analytics, the Advanced enterprise Power BI dashboard, and strategic business conclusions.",

        # Slide 3: Acknowledgement
        "First, I would like to express my sincere gratitude to the ShadowFox team and my mentor, Mr. Aakash, for their guidance, "
        "and I affirm that all analytics, models, and code presented in this portfolio were independently developed and programmatically verified.",

        # Slide 4: Beginner Overview
        "Starting with the Beginner Level, Project 1 focused on small business retail sales performance. "
        "I built an automated Python cleaning pipeline resolving duplicate orders, irregular formatting, and null values across 1,250 verified transactions, followed by a dynamic Excel dashboard.",

        # Slide 5: Monthly Sales Trend
        "Examining the monthly sales trend, the business achieved strong seasonality with sales peaking in November at $23,036, "
        "driven by holiday demand and larger basket sizes, rebounding from a mid-year trough in June of $9,972.",

        # Slide 6: Category Profitability
        "Looking at category profitability, Furniture and Electronics generated 79 percent of total gross revenue. "
        "While the Ergonomic Office Chair was our highest revenue product at over $43,000, our highest margin items were accessories, led by Gel Ink Pens at a 67.7 percent profit margin.",

        # Slide 7: Regional Performance & Excel
        "Geographically, the West territory led all regions in sales volume and profitability. "
        "To empower business managers, I consolidated these metrics into an automated four-tab Excel workbook featuring dynamic formulas, automated KPI cards, and embedded charts.",

        # Slide 8: Intermediate Overview
        "Moving to the Intermediate Level, Project 2 evaluated customer behaviour, revenue concentration, and retention dynamics "
        "across a 24-month e-commerce dataset spanning 850 accounts and 2,306 transactions.",

        # Slide 9: Repeat vs One-Time
        "Our spend analysis revealed striking repeat buyer asymmetry. "
        "Repeat customers represent only 47 percent of accounts, yet they generate 80.88 percent of total revenue, delivering an average lifetime value 4.8 times greater than one-time purchasers.",

        # Slide 10: RFM Segmentation
        "Using Recency, Frequency, and Monetary scoring, I categorized accounts into eight distinct behavioral segments. "
        "Our top 200 Champions alone drive nearly 50 percent of total company sales, confirming high revenue concentration.",

        # Slide 11: Cohort Retention
        "Tracking monthly customer cohorts across 24 months showed that the sharpest customer drop-off occurs between month 0 and month 1, "
        "where retention drops to approximately 20 percent, before stabilizing into a loyal, predictable long-term baseline between 12 and 16 percent.",

        # Slide 12: SQL Architecture
        "To support rigorous querying, I loaded the cleaned data into an SQLite relational database and executed 10 production SQL queries "
        "leveraging Common Table Expressions and Window Functions including DENSE_RANK, LAG for month-over-month trends, and NTILE for spend quintiles.",

        # Slide 13: Advanced Overview
        "Progressing to the Advanced Level, Project 3 engineered an enterprise Business Intelligence architecture using Microsoft Power BI, "
        "modeling 3 years of enterprise operations into a certified six-table Star Schema.",

        # Slide 14: Power BI Scorecard
        "Over the three-year timeline, enterprise gross revenue expanded from $542,000 to $2.93 Million, generating $1.12 Million in net profit "
        "with an operating margin of 38.4 percent, powered by 28 production DAX measures.",

        # Slide 15: Logistics SLA
        "Our supply chain analysis revealed an operational risk. Overall on-time delivery compliance sits at 68.8 percent against an 85 percent target, "
        "with Standard Class shipping identified as the primary ground freight bottleneck at only 59.2 percent on-time compliance.",

        # Slide 16: Conclusion
        "In conclusion, this portfolio delivers an actionable roadmap: seasonal inventory stocking, proactive onboarding to retain month-one customers, "
        "and logistics SLA renegotiation to safeguard customer experience and margin growth.",

        # Slide 17: Thank You
        "Thank you to ShadowFox and Mr. Aakash for this invaluable internship experience. "
        "All code, SQL scripts, models, and reports are fully available on my GitHub repository. Thank you!"
    ]

    # 2. Export Slides as PNG using PowerPoint COM
    print("Exporting presentation slides as high-res images...")
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    pres = ppt.Presentations.Open(pptx_path, WithWindow=1)
    
    slide_images = []
    slide_count = pres.Slides.Count
    print(f"Presentation loaded with {slide_count} slides.")

    for i in range(slide_count):
        img_file = os.path.join(temp_dir, f"slide_{i+1:02d}.png")
        # Export as 1920x1080 HD
        pres.Slides[i].Export(img_file, "PNG", 1920, 1080)
        slide_images.append(img_file)
        print(f"  Slide {i+1} exported to image.")

    pres.Close()
    ppt.Quit()

    # 3. Synthesize Voice Audio for each slide
    print("\nSynthesizing voice narration with SAPI...")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # Choose Zira voice if available
    for voice in speaker.GetVoices():
        if "Zira" in voice.GetDescription():
            speaker.Voice = voice
            print("  Selected Voice:", voice.GetDescription())
            break
    speaker.Rate = 0 # Normal speaking rate

    audio_files = []
    durations = []

    for i, text in enumerate(narrations):
        wav_file = os.path.join(temp_dir, f"audio_{i+1:02d}.wav")
        stream = win32com.client.Dispatch("SAPI.SpFileStream")
        stream.Open(wav_file, 3) # SSFMCreateForWrite
        speaker.AudioOutputStream = stream
        speaker.Speak(text)
        stream.Close()

        with wave.open(wav_file, "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            duration = frames / float(rate)

        audio_files.append(wav_file)
        durations.append(duration)
        print(f"  Slide {i+1} audio generated: {duration:.2f} seconds.")

    total_duration = sum(durations)
    print(f"\nTotal video duration will be: {total_duration/60.0:.2f} minutes ({total_duration:.1f} seconds).")

    # 4. Generate MP4 segment for each slide using FFmpeg
    print("\nEncoding slide video segments with FFmpeg...")
    segment_files = []
    for i in range(slide_count):
        seg_file = os.path.join(temp_dir, f"segment_{i+1:02d}.mp4")
        img_file = slide_images[i]
        wav_file = audio_files[i]
        dur = durations[i] + 0.8 # add 0.8s pause at end of each slide for natural transition

        if os.path.exists(seg_file) and os.path.getsize(seg_file) > 1000:
            print(f"  Segment {i+1} already exists, skipping.")
            segment_files.append(seg_file)
            continue

        cmd = [
            ffmpeg_exe,
            "-y",
            "-loop", "1",
            "-i", img_file,
            "-i", wav_file,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", f"{dur:.2f}",
            "-shortest",
            seg_file
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print(f"Error encoding segment {i+1}:", res.stderr.decode("utf-8", errors="ignore"))
            return False
        segment_files.append(seg_file)
        print(f"  Segment {i+1} encoded.")

    # 5. Concatenate segments into final master MP4
    print("\nConcatenating all segments into master MP4 video...")
    concat_list_file = os.path.join(temp_dir, "concat_list.txt")
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for seg in segment_files:
            # Format for ffmpeg concat demuxer
            clean_path = seg.replace("\\", "/")
            f.write(f"file '{clean_path}'\n")

    out_mp4_1 = os.path.join(base_dir, r"ShadowFox_Internship_Documentation\Presentation\ShadowFox_Data_Analyst_Internship_Presentation.mp4")
    out_mp4_2 = os.path.join(base_dir, r"Internship_Documentation\ShadowFox_Internship_Documentation\Presentation\ShadowFox_Data_Analyst_Internship_Presentation.mp4")

    cmd_concat = [
        ffmpeg_exe,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        out_mp4_1
    ]
    res_concat = subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res_concat.returncode != 0:
        print("Error concatenating master MP4:", res_concat.stderr.decode("utf-8", errors="ignore"))
        return False

    # Also copy to mirror folder
    import shutil
    shutil.copy2(out_mp4_1, out_mp4_2)

    size_mb = os.path.getsize(out_mp4_1) / (1024 * 1024)
    print(f"\n Master Presentation Video Successfully Generated!")
    print(f"  Path: {out_mp4_1}")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Duration: {total_duration/60.0:.2f} minutes")
    return True

if __name__ == "__main__":
    generate_video()
