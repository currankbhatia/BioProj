import java.util.*;
import java.io.*;
import static java.lang.Math.*;

public class globalAlign{
/*
	A 		C 		G 		T
A	91		-114	-31		-123
C	-114	100		-125	-31
G	-31		-125	100		-114
T	-123	-31		-114	91
*/

	public static String randomSequence(int L)
	{
		String output="";
		char[] nucleotides = {'A','G','C','T'};

		for(int i=0; i<L; i++)
		{
			int temp = (int)(random()*4);
			char nuc = nucleotides[temp];
			output+=""+nuc;
		}
		return output;
	}

	public static String seqToSeq(String original)
	{
		int size = original.length();
		int changes = size/10;

		char[] nucleotides = {'A','G','C','T'};

		char[] startArray = original.toCharArray();

		for(int i=0; i<10; i++)
		{
			int randomPosition = (int)(random()*size);
			int randomNuc = (int)(random()*4);

			char nuc = nucleotides[randomNuc];
			startArray[randomPosition] = nuc;
		}
		String temp = new String(startArray);
		String ret = "" + temp;

		return ret;

	}

	public static void main(String[] args)
	{
		try {
			PrintStream out = new PrintStream(new FileOutputStream("aln10.txt"));

			/*String psd = "AATATAACCCAATAATTTTAACTAGCTCGCAGGAGCGAGGCATCCTTGCATCCTTGCATCCTTCCCGGTTACAGTTACCCGGTACTGCATAACAATGAACCCGAAACTGGGACAGATCGGAGATGGTGTGTGTGTGCTTCTCGCTGTGTGTGCCGTGTTAATCCGTTTGCCATCAGCCAGATTATTAGTCAATTGCAGTTACAGAGTTTCGCTTTCGTCCTCGTTTCACTTTCGAGTTAGCCTTTATTGCAGCATCTTGAACAATCGGCGCAGTTTGGTAACACGCTGTGCCCTAGCCCTACTTTCCCCGGCCGATTCAGCGGATTTAGACGGAATCGAGGGACCCTGACTGCACTCGGTTCGTTATATGAAACCGAAAACAAAACCTTAACCGGGTTGCAAAGTCAGGGCATTCCGACGATCTCGCCATATCCATCGCCATCGCCATCTTCTGCGGGCGTTTGTTTGTTTGTTTGCTGGGATTAGCCAAGGGCTTGACTTGGAACCCGATCGTCCCTTTTCATTAGAAAGTCATAAAAACACATAATAATGATGTCGAACGGATTAGGGACGCGACTCGCAAGTCCAGGCAGCGCAATTAACGGACTAGCGAACTGGGTTATTTTTTGCGCCGACTTAGCCCTGATCCGCGAGCTTAACCCGTTTGAGCCGCCAGTCGAGCAGGTAGTTCCTGCCCACAC";

			String mel ="AATATAACCCAATAATTTGAAGTAACTGGCAGGAGCGAGGTATCCTTCCTGGTTACCCGGTACTGCATAACAATGGAACCCGAACCGTAACTGGGACAGATCGAAAAGCTGGCCTGGTTTCTCGCTGTGTGTGCCGTGTTAATCCGTTTGCCATCAGCGAGATTATTAGTCAATTGCAGTTGCAGCGTTTCGCTTTCGTCCTCGTTTCACTTTCGAGTTAGACTTTATTGCAGCATCTTGAACAATCGTCGCAGTTTGGTAACACGCTGTGCCATACTTTCATTTAGACGGAATCGAGGGACCCTGGACTATAATCGCACAACGAGACCGGGTTGCGAAGTCAGGGCATTCCGCCGATCTAGCCATCGCCATCTTCTGCGGGCGTTTGTTTGTTTGTTTGCTGGGATTAGCCAAGGGCTTGACTTGGAATCCAATCCCGATCCCTAGCCCGATCCCAATCCCAATCCCAATCCCTTGTCCTTTTCATTAGAAAGTCATAAAAACACATAATAATGATGTCGAAGGGATTAGGGGCGCGCAGGTCCAGGCAACGCAATTAACGGACTAGCGAACTGGGTTATTTTTTTGCGCCGACTTAGCCCTGATCCGCGAGCTTAACCCGTTTTGAGCCGGGCAGCAGGTAGTTGTGGGTGGACCCCACGA";
*/

			String psd = randomSequence(100);

			String mel = seqToSeq(psd);

			out.println("Sequence 1: "+psd);
			out.println("Sequence 2: "+mel);
			//out.println(mel);

			Map<String,Integer> subs = new HashMap<String,Integer>(16);

			subs.put("AA",91);
			subs.put("AC",-114);
			subs.put("AG",-31);
			subs.put("AT",-123);
			subs.put("CA",-114);
			subs.put("CC",100);
			subs.put("CG",-125);
			subs.put("CT",-31);
			subs.put("GA",-31);
			subs.put("GC",-125);
			subs.put("GG",100);
			subs.put("GT",-114);
			subs.put("TA",-123);
			subs.put("TC",-31);
			subs.put("TG",-114);
			subs.put("TT",91);

			int gap = -500;

			String temp= "";

			int[][] option = new int[psd.length()+1][mel.length()+1];

			for(int i=1; i<=psd.length(); i++)
			{
				option[i][0] = option[i-1][0] + gap;
			}

			for(int j=1; j<=mel.length(); j++)
			{
				option[0][j] = option[0][j-1] + gap;
			}

			for(int d = 1; d <= psd.length(); d++)
			{
				for(int f = 1; f<= mel.length(); f++)
				{
					char seq1 = psd.charAt(d-1);
					char seq2 = mel.charAt(f-1);
					temp = "" + seq1 + seq2;

					Integer addon = subs.get(temp);

					int scoredrop = option[d-1][f-1] + addon;

					int scoreleft = option[d][f-1] + gap;

					int scoreup = option[d-1][f] + gap;

					option[d][f] = Math.max(Math.max(scoredrop,scoreleft),scoreup);
				}

			}

			/*for(int i = 0; i<psd.length(); i++)
			{
				for(int j = 0; j<mel.length(); j++)
				{
					out.print(option[i][j] + "\t");
				}
				out.println();
			}*/

			out.println("The optimal alignment between the given sequences has a score of "+option[psd.length()][mel.length()]);
			/*String dank = randomSequence(5);
			out.println(dank);*/
		}
		catch(FileNotFoundException e) {
			System.out.println("File doesn't exist");
		}
	}

}
